const {ESLintUtils, AST_NODE_TYPES} = require('@typescript-eslint/utils');

const fs = require("fs")
const path = require("path")

const createRule = ESLintUtils.RuleCreator((name) => name);

/**
 * Strategy:
 *  1. Pass over all useQuery calls and append "Variables" to the identifierName of the first type
 *    -- eg: useQuery<SomeQuery>() --> SomeQueryVariables
 *  2. Check if "SomeQueryVariables" is exported from the file that "SomeQuery" is imported from.
 *  3. If it's not then continue
 *     If it is then check that the second type argument to useQuery is that SomeQueryVariables.
 *     If not then throw an error.
 *  
 * TODO: Add auto-fixer
 */

module.exports = { 
  rule: createRule({
    create(context) {
      return {
        [AST_NODE_TYPES.CallExpression](node) {
          const callee = node.callee;
          if (callee.type !== 'Identifier') {
            return;
          }
          // if it's not a useQuery call then ignore
          if (callee.name !== 'useQuery') {
            return;
          }
<<<<<<< Updated upstream
          const queryType = node.typeParameters?.params?.[0];
=======
          const queryType = node.typeParameters && node.typeParameters.params && node.typeParameters.params[0];
>>>>>>> Stashed changes
          if (!queryType || queryType.type !== 'TSTypeReference') {
            return;
          }
          if (queryType.typeName.type !== 'Identifier') {
            return;
          }
          const queryName = queryType.typeName.name;
          // if the type doesn't end with Query then ignore
          if (!queryName.endsWith('Query')) {
            return;
          }
          const variablesName = queryName + 'Variables';
          const importPath = context.getSourceCode().ast.body.find(node => 
            node.type === 'ImportDeclaration' && 
            node.specifiers.find(
              node => node.type === 'ImportSpecifier' && node.local.name === queryName
            )
          ).source.value
          const currentPath = context.getFilename().split('/').slice(0, -1).join('/')
            const fullPath = path.join(currentPath,  importPath + '.ts');

          const graphqlTypeFile = fs.readFileSync(fullPath, {encoding:'utf8'});
          
          // This part is kind of hacky. I should use the parser service to find the identifier
          // but this is faster then tokenizing the whole file
          if (!graphqlTypeFile.includes('export interface '+variablesName)) {
            return;
          }
          // This is a Query type with a generated QueryVariables type. Make sure we're using it
          const secondType = node.typeParameters.params[1];
          if (
            !secondType ||
            (secondType.type === 'TSTypeReference' &&
              secondType.typeName.type === 'Identifier' &&
              secondType.typeName.name !== variablesName)
          ) {
            context.report({
              messageId: 'missing-graphql-variables-type',
              node,
              data: {
                queryType: queryName,
                variablesType: variablesName,
              }
            });
          }
        },
      };
    },
    name: 'missing-graphql-variables-type',
    meta: {
      docs: {
        description: 'useQuery is missing QueryVariables parameter.',
        recommended: 'error',
      },
      messages: {
        'missing-graphql-variables-type': '`useQuery<{{queryType}}>(...)` should be `useQuery<{{queryType}},{{variablesType}}>(...)`.',
      },
      type: 'problem',
      schema: [],
    },
    defaultOptions: [],
  })
}