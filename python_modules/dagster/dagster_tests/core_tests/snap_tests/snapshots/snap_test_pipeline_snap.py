# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_basic_dep_fan_out 1'] = '''{
  "__class__": "PipelineSnapshot",
  "config_schema_snapshot": {
    "__class__": "ConfigSchemaSnapshot",
    "all_config_snaps_by_key": {
      "Any": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": "Any",
        "key": "Any",
        "kind": {
          "__enum__": "ConfigTypeKind.ANY"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
        ]
      },
      "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
        ]
      },
      "Array.String": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.String",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.String",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String"
        ]
      },
      "Bool": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Bool",
        "key": "Bool",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.BOOL"
        },
        "type_param_keys": null
      },
      "Float": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Float",
        "key": "Float",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.FLOAT"
        },
        "type_param_keys": null
      },
      "Int": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Int",
        "key": "Int",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.INT"
        },
        "type_param_keys": null
      },
      "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Bool",
          "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59"
        ]
      },
      "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Float",
          "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3"
        ]
      },
      "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Int",
          "Selector.a9799b971d12ace70a2d8803c883c863417d0725"
        ]
      },
      "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Selector.e04723c9d9937e3ab21206435b22247cfbe58269"
        ]
      },
      "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
        ]
      },
      "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute all steps in a single process.",
            "is_required": false,
            "name": "in_process",
            "type_key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute each step in an individual process.",
            "is_required": false,
            "name": "multiprocess",
            "type_key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1"
          }
        ],
        "given_name": null,
        "key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "disabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "enabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `forkserver`.",
            "is_required": false,
            "name": "forkserver",
            "type_key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `spawn`.",
            "is_required": false,
            "name": "spawn",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Int"
          }
        ],
        "given_name": null,
        "key": "Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Float"
          }
        ],
        "given_name": null,
        "key": "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          }
        ],
        "given_name": null,
        "key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.081354663b9d4b8fbfd1cb8e358763912953913f": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"INFO\\"",
            "description": "The logger\'s threshold.",
            "is_required": false,
            "name": "log_level",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"dagster\\"",
            "description": "The name of your logger.",
            "is_required": false,
            "name": "name",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "key",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "limit",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "value",
            "type_key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
          }
        ],
        "given_name": null,
        "key": "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          }
        ],
        "given_name": null,
        "key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
            "is_required": false,
            "name": "io_manager",
            "type_key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7"
          }
        ],
        "given_name": null,
        "key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "applyLimitPerUniqueValue",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "result",
            "type_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742"
          }
        ],
        "given_name": null,
        "key": "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "[DEPRECATED]",
            "is_required": false,
            "name": "marker_to_close",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          }
        ],
        "given_name": null,
        "key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.453a16b50ebe4c3d1abfd68ad3001f366304f948": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "passone",
            "type_key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "passtwo",
            "type_key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "return_one",
            "type_key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5"
          }
        ],
        "given_name": null,
        "key": "Shape.453a16b50ebe4c3d1abfd68ad3001f366304f948",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "path",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Explicitly specify the modules to preload in the forkserver. Otherwise, there are two cases for default values if modules are not specified. If the Dagster job was loaded from a module, the same module will be preloaded. If not, the `dagster` module is preloaded.",
            "is_required": false,
            "name": "preload_modules",
            "type_key": "Array.String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.60acefe08e1243b47034a632522b12985eb4acd1": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "0",
            "description": "The number of processes that may run concurrently. By default, this is set to be the return value of `multiprocessing.cpu_count()`.",
            "is_required": false,
            "name": "max_concurrent",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Select how subprocesses are created. By default, `spawn` is selected. See https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods.",
            "is_required": false,
            "name": "start_method",
            "type_key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "A set of limits that are applied to steps with particular tags. If a value is set, the limit is applied to only that key-value pair. If no value is set, the limit is applied across all values of that key. If the value is set to a dict with `applyLimitPerUniqueValue: true`, the limit will apply to the number of unique values for that key. Note that these limits are per run, not global.",
            "is_required": false,
            "name": "tag_concurrency_limits",
            "type_key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
          }
        ],
        "given_name": null,
        "key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.638bf47eadd4d4ff7beb154f33a54f6ace55e31f": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"config\\": {\\"multiprocess\\": {\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}}}",
            "description": "Configure how steps are executed within a run.",
            "is_required": false,
            "name": "execution",
            "type_key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure how loggers emit messages within a run.",
            "is_required": false,
            "name": "loggers",
            "type_key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"passone\\": {}, \\"passtwo\\": {}, \\"return_one\\": {}}",
            "description": "Configure runtime parameters for ops or assets.",
            "is_required": false,
            "name": "ops",
            "type_key": "Shape.453a16b50ebe4c3d1abfd68ad3001f366304f948"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"io_manager\\": {}}",
            "description": "Configure how shared resources are implemented within a run.",
            "is_required": false,
            "name": "resources",
            "type_key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778"
          }
        ],
        "given_name": null,
        "key": "Shape.638bf47eadd4d4ff7beb154f33a54f6ace55e31f",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.743e47901855cb245064dd633e217bfcb49a11a7": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [],
        "given_name": null,
        "key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "outputs",
            "type_key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
          }
        ],
        "given_name": null,
        "key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "console",
            "type_key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a"
          }
        ],
        "given_name": null,
        "key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"multiprocess\\": {}}",
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2"
          }
        ],
        "given_name": null,
        "key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "String": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "String",
        "key": "String",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.STRING"
        },
        "type_param_keys": null
      }
    }
  },
  "dagster_type_namespace_snapshot": {
    "__class__": "DagsterTypeNamespaceSnapshot",
    "all_dagster_type_snaps_by_key": {
      "Any": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Any",
        "is_builtin": true,
        "key": "Any",
        "kind": {
          "__enum__": "DagsterTypeKind.ANY"
        },
        "loader_schema_key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Any",
        "type_param_keys": []
      },
      "Bool": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Bool",
        "is_builtin": true,
        "key": "Bool",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Bool",
        "type_param_keys": []
      },
      "Float": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Float",
        "is_builtin": true,
        "key": "Float",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Float",
        "type_param_keys": []
      },
      "Int": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Int",
        "is_builtin": true,
        "key": "Int",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Int",
        "type_param_keys": []
      },
      "Nothing": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Nothing",
        "is_builtin": true,
        "key": "Nothing",
        "kind": {
          "__enum__": "DagsterTypeKind.NOTHING"
        },
        "loader_schema_key": null,
        "materializer_schema_key": null,
        "name": "Nothing",
        "type_param_keys": []
      },
      "String": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "String",
        "is_builtin": true,
        "key": "String",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "String",
        "type_param_keys": []
      }
    }
  },
  "dep_structure_snapshot": {
    "__class__": "DependencyStructureSnapshot",
    "solid_invocation_snaps": [
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [
          {
            "__class__": "InputDependencySnap",
            "input_name": "value",
            "is_dynamic_collect": false,
            "upstream_output_snaps": [
              {
                "__class__": "OutputHandleSnap",
                "output_name": "result",
                "solid_name": "return_one"
              }
            ]
          }
        ],
        "is_dynamic_mapped": false,
        "solid_def_name": "passthrough",
        "solid_name": "passone",
        "tags": {}
      },
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [
          {
            "__class__": "InputDependencySnap",
            "input_name": "value",
            "is_dynamic_collect": false,
            "upstream_output_snaps": [
              {
                "__class__": "OutputHandleSnap",
                "output_name": "result",
                "solid_name": "return_one"
              }
            ]
          }
        ],
        "is_dynamic_mapped": false,
        "solid_def_name": "passthrough",
        "solid_name": "passtwo",
        "tags": {}
      },
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [],
        "is_dynamic_mapped": false,
        "solid_def_name": "return_one",
        "solid_name": "return_one",
        "tags": {}
      }
    ]
  },
  "description": null,
  "graph_def_name": "single_dep_job",
  "lineage_snapshot": null,
  "mode_def_snaps": [
    {
      "__class__": "ModeDefSnap",
      "description": null,
      "logger_def_snaps": [
        {
          "__class__": "LoggerDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          },
          "description": "The default colored console logger.",
          "name": "console"
        }
      ],
      "name": "default",
      "resource_def_snaps": [
        {
          "__class__": "ResourceDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
          "name": "io_manager"
        }
      ],
      "root_config_key": "Shape.638bf47eadd4d4ff7beb154f33a54f6ace55e31f"
    }
  ],
  "name": "single_dep_job",
  "solid_definitions_snapshot": {
    "__class__": "SolidDefinitionsSnapshot",
    "composite_solid_def_snaps": [],
    "solid_def_snaps": [
      {
        "__class__": "SolidDefSnap",
        "config_field_snap": {
          "__class__": "ConfigFieldSnap",
          "default_provided": false,
          "default_value_as_json_str": null,
          "description": null,
          "is_required": false,
          "name": "config",
          "type_key": "Any"
        },
        "description": null,
        "input_def_snaps": [
          {
            "__class__": "InputDefSnap",
            "dagster_type_key": "Int",
            "description": null,
            "name": "value"
          }
        ],
        "name": "passthrough",
        "output_def_snaps": [
          {
            "__class__": "OutputDefSnap",
            "dagster_type_key": "Any",
            "description": null,
            "is_dynamic": false,
            "is_required": true,
            "name": "result"
          }
        ],
        "required_resource_keys": [],
        "tags": {}
      },
      {
        "__class__": "SolidDefSnap",
        "config_field_snap": {
          "__class__": "ConfigFieldSnap",
          "default_provided": false,
          "default_value_as_json_str": null,
          "description": null,
          "is_required": false,
          "name": "config",
          "type_key": "Any"
        },
        "description": null,
        "input_def_snaps": [],
        "name": "return_one",
        "output_def_snaps": [
          {
            "__class__": "OutputDefSnap",
            "dagster_type_key": "Any",
            "description": null,
            "is_dynamic": false,
            "is_required": true,
            "name": "result"
          }
        ],
        "required_resource_keys": [],
        "tags": {}
      }
    ]
  },
  "tags": {}
}'''

snapshots['test_basic_dep_fan_out 2'] = '705d18fc197ab82461b64d32ff1fd2f793b97d43'

snapshots['test_basic_fan_in 1'] = '''{
  "__class__": "PipelineSnapshot",
  "config_schema_snapshot": {
    "__class__": "ConfigSchemaSnapshot",
    "all_config_snaps_by_key": {
      "Any": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": "Any",
        "key": "Any",
        "kind": {
          "__enum__": "ConfigTypeKind.ANY"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
        ]
      },
      "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
        ]
      },
      "Array.String": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.String",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.String",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String"
        ]
      },
      "Bool": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Bool",
        "key": "Bool",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.BOOL"
        },
        "type_param_keys": null
      },
      "Float": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Float",
        "key": "Float",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.FLOAT"
        },
        "type_param_keys": null
      },
      "Int": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Int",
        "key": "Int",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.INT"
        },
        "type_param_keys": null
      },
      "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Bool",
          "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59"
        ]
      },
      "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Float",
          "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3"
        ]
      },
      "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Int",
          "Selector.a9799b971d12ace70a2d8803c883c863417d0725"
        ]
      },
      "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Selector.e04723c9d9937e3ab21206435b22247cfbe58269"
        ]
      },
      "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
        ]
      },
      "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute all steps in a single process.",
            "is_required": false,
            "name": "in_process",
            "type_key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute each step in an individual process.",
            "is_required": false,
            "name": "multiprocess",
            "type_key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1"
          }
        ],
        "given_name": null,
        "key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "disabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "enabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `forkserver`.",
            "is_required": false,
            "name": "forkserver",
            "type_key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `spawn`.",
            "is_required": false,
            "name": "spawn",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Int"
          }
        ],
        "given_name": null,
        "key": "Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Float"
          }
        ],
        "given_name": null,
        "key": "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          }
        ],
        "given_name": null,
        "key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.081354663b9d4b8fbfd1cb8e358763912953913f": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"INFO\\"",
            "description": "The logger\'s threshold.",
            "is_required": false,
            "name": "log_level",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"dagster\\"",
            "description": "The name of your logger.",
            "is_required": false,
            "name": "name",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "key",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "limit",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "value",
            "type_key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
          }
        ],
        "given_name": null,
        "key": "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          }
        ],
        "given_name": null,
        "key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
            "is_required": false,
            "name": "io_manager",
            "type_key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7"
          }
        ],
        "given_name": null,
        "key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "applyLimitPerUniqueValue",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.3856bf4e41e3c0ab0e99ddc34cc91a8e423a14c8": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"config\\": {\\"multiprocess\\": {\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}}}",
            "description": "Configure how steps are executed within a run.",
            "is_required": false,
            "name": "execution",
            "type_key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure how loggers emit messages within a run.",
            "is_required": false,
            "name": "loggers",
            "type_key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"nothing_one\\": {}, \\"nothing_two\\": {}, \\"take_nothings\\": {}}",
            "description": "Configure runtime parameters for ops or assets.",
            "is_required": false,
            "name": "ops",
            "type_key": "Shape.ab651c1dba946d13580db07a91f4d107190118ae"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"io_manager\\": {}}",
            "description": "Configure how shared resources are implemented within a run.",
            "is_required": false,
            "name": "resources",
            "type_key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778"
          }
        ],
        "given_name": null,
        "key": "Shape.3856bf4e41e3c0ab0e99ddc34cc91a8e423a14c8",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "result",
            "type_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742"
          }
        ],
        "given_name": null,
        "key": "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "[DEPRECATED]",
            "is_required": false,
            "name": "marker_to_close",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          }
        ],
        "given_name": null,
        "key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "path",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Explicitly specify the modules to preload in the forkserver. Otherwise, there are two cases for default values if modules are not specified. If the Dagster job was loaded from a module, the same module will be preloaded. If not, the `dagster` module is preloaded.",
            "is_required": false,
            "name": "preload_modules",
            "type_key": "Array.String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.60acefe08e1243b47034a632522b12985eb4acd1": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "0",
            "description": "The number of processes that may run concurrently. By default, this is set to be the return value of `multiprocessing.cpu_count()`.",
            "is_required": false,
            "name": "max_concurrent",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Select how subprocesses are created. By default, `spawn` is selected. See https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods.",
            "is_required": false,
            "name": "start_method",
            "type_key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "A set of limits that are applied to steps with particular tags. If a value is set, the limit is applied to only that key-value pair. If no value is set, the limit is applied across all values of that key. If the value is set to a dict with `applyLimitPerUniqueValue: true`, the limit will apply to the number of unique values for that key. Note that these limits are per run, not global.",
            "is_required": false,
            "name": "tag_concurrency_limits",
            "type_key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
          }
        ],
        "given_name": null,
        "key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.743e47901855cb245064dd633e217bfcb49a11a7": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.ab651c1dba946d13580db07a91f4d107190118ae": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "nothing_one",
            "type_key": "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "nothing_two",
            "type_key": "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "take_nothings",
            "type_key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5"
          }
        ],
        "given_name": null,
        "key": "Shape.ab651c1dba946d13580db07a91f4d107190118ae",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [],
        "given_name": null,
        "key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "outputs",
            "type_key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
          }
        ],
        "given_name": null,
        "key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "console",
            "type_key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a"
          }
        ],
        "given_name": null,
        "key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"multiprocess\\": {}}",
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2"
          }
        ],
        "given_name": null,
        "key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "String": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "String",
        "key": "String",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.STRING"
        },
        "type_param_keys": null
      }
    }
  },
  "dagster_type_namespace_snapshot": {
    "__class__": "DagsterTypeNamespaceSnapshot",
    "all_dagster_type_snaps_by_key": {
      "Any": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Any",
        "is_builtin": true,
        "key": "Any",
        "kind": {
          "__enum__": "DagsterTypeKind.ANY"
        },
        "loader_schema_key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Any",
        "type_param_keys": []
      },
      "Bool": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Bool",
        "is_builtin": true,
        "key": "Bool",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Bool",
        "type_param_keys": []
      },
      "Float": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Float",
        "is_builtin": true,
        "key": "Float",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Float",
        "type_param_keys": []
      },
      "Int": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Int",
        "is_builtin": true,
        "key": "Int",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Int",
        "type_param_keys": []
      },
      "Nothing": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Nothing",
        "is_builtin": true,
        "key": "Nothing",
        "kind": {
          "__enum__": "DagsterTypeKind.NOTHING"
        },
        "loader_schema_key": null,
        "materializer_schema_key": null,
        "name": "Nothing",
        "type_param_keys": []
      },
      "String": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "String",
        "is_builtin": true,
        "key": "String",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "String",
        "type_param_keys": []
      }
    }
  },
  "dep_structure_snapshot": {
    "__class__": "DependencyStructureSnapshot",
    "solid_invocation_snaps": [
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [],
        "is_dynamic_mapped": false,
        "solid_def_name": "return_nothing",
        "solid_name": "nothing_one",
        "tags": {}
      },
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [],
        "is_dynamic_mapped": false,
        "solid_def_name": "return_nothing",
        "solid_name": "nothing_two",
        "tags": {}
      },
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [
          {
            "__class__": "InputDependencySnap",
            "input_name": "nothing",
            "is_dynamic_collect": false,
            "upstream_output_snaps": [
              {
                "__class__": "OutputHandleSnap",
                "output_name": "result",
                "solid_name": "nothing_one"
              },
              {
                "__class__": "OutputHandleSnap",
                "output_name": "result",
                "solid_name": "nothing_two"
              }
            ]
          }
        ],
        "is_dynamic_mapped": false,
        "solid_def_name": "take_nothings",
        "solid_name": "take_nothings",
        "tags": {}
      }
    ]
  },
  "description": null,
  "graph_def_name": "fan_in_test",
  "lineage_snapshot": null,
  "mode_def_snaps": [
    {
      "__class__": "ModeDefSnap",
      "description": null,
      "logger_def_snaps": [
        {
          "__class__": "LoggerDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          },
          "description": "The default colored console logger.",
          "name": "console"
        }
      ],
      "name": "default",
      "resource_def_snaps": [
        {
          "__class__": "ResourceDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
          "name": "io_manager"
        }
      ],
      "root_config_key": "Shape.3856bf4e41e3c0ab0e99ddc34cc91a8e423a14c8"
    }
  ],
  "name": "fan_in_test",
  "solid_definitions_snapshot": {
    "__class__": "SolidDefinitionsSnapshot",
    "composite_solid_def_snaps": [],
    "solid_def_snaps": [
      {
        "__class__": "SolidDefSnap",
        "config_field_snap": {
          "__class__": "ConfigFieldSnap",
          "default_provided": false,
          "default_value_as_json_str": null,
          "description": null,
          "is_required": false,
          "name": "config",
          "type_key": "Any"
        },
        "description": null,
        "input_def_snaps": [],
        "name": "return_nothing",
        "output_def_snaps": [
          {
            "__class__": "OutputDefSnap",
            "dagster_type_key": "Nothing",
            "description": null,
            "is_dynamic": false,
            "is_required": true,
            "name": "result"
          }
        ],
        "required_resource_keys": [],
        "tags": {}
      },
      {
        "__class__": "SolidDefSnap",
        "config_field_snap": {
          "__class__": "ConfigFieldSnap",
          "default_provided": false,
          "default_value_as_json_str": null,
          "description": null,
          "is_required": false,
          "name": "config",
          "type_key": "Any"
        },
        "description": null,
        "input_def_snaps": [
          {
            "__class__": "InputDefSnap",
            "dagster_type_key": "Nothing",
            "description": null,
            "name": "nothing"
          }
        ],
        "name": "take_nothings",
        "output_def_snaps": [
          {
            "__class__": "OutputDefSnap",
            "dagster_type_key": "Any",
            "description": null,
            "is_dynamic": false,
            "is_required": true,
            "name": "result"
          }
        ],
        "required_resource_keys": [],
        "tags": {}
      }
    ]
  },
  "tags": {}
}'''

snapshots['test_basic_fan_in 2'] = '076f986d986b3bbbdac6cccf1a5c6ca0542764ee'

snapshots['test_deserialize_solid_def_snaps_multi_type_config 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": null,
  "enum_values": null,
  "fields": [
    {
      "__class__": "ConfigFieldSnap",
      "default_provided": false,
      "default_value_as_json_str": null,
      "description": null,
      "is_required": true,
      "name": "bar",
      "type_key": "Selector.c12ab659793f168246640a294e913ac9d90a242a"
    },
    {
      "__class__": "ConfigFieldSnap",
      "default_provided": false,
      "default_value_as_json_str": null,
      "description": null,
      "is_required": true,
      "name": "foo",
      "type_key": "Array.Float"
    }
  ],
  "given_name": null,
  "key": "Permissive.bda2965be6725b48329d76783336ed442951fd54",
  "kind": {
    "__enum__": "ConfigTypeKind.PERMISSIVE_SHAPE"
  },
  "scalar_kind": null,
  "type_param_keys": null
}'''

snapshots['test_empty_pipeline_snap_props 1'] = '''{
  "__class__": "PipelineSnapshot",
  "config_schema_snapshot": {
    "__class__": "ConfigSchemaSnapshot",
    "all_config_snaps_by_key": {
      "Any": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": "Any",
        "key": "Any",
        "kind": {
          "__enum__": "ConfigTypeKind.ANY"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
        ]
      },
      "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
        ]
      },
      "Array.String": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.String",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.String",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String"
        ]
      },
      "Bool": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Bool",
        "key": "Bool",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.BOOL"
        },
        "type_param_keys": null
      },
      "Float": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Float",
        "key": "Float",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.FLOAT"
        },
        "type_param_keys": null
      },
      "Int": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Int",
        "key": "Int",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.INT"
        },
        "type_param_keys": null
      },
      "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Bool",
          "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59"
        ]
      },
      "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Float",
          "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3"
        ]
      },
      "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Int",
          "Selector.a9799b971d12ace70a2d8803c883c863417d0725"
        ]
      },
      "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Selector.e04723c9d9937e3ab21206435b22247cfbe58269"
        ]
      },
      "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
        ]
      },
      "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute all steps in a single process.",
            "is_required": false,
            "name": "in_process",
            "type_key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute each step in an individual process.",
            "is_required": false,
            "name": "multiprocess",
            "type_key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1"
          }
        ],
        "given_name": null,
        "key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "disabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "enabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `forkserver`.",
            "is_required": false,
            "name": "forkserver",
            "type_key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `spawn`.",
            "is_required": false,
            "name": "spawn",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Int"
          }
        ],
        "given_name": null,
        "key": "Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Float"
          }
        ],
        "given_name": null,
        "key": "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          }
        ],
        "given_name": null,
        "key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.081354663b9d4b8fbfd1cb8e358763912953913f": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"INFO\\"",
            "description": "The logger\'s threshold.",
            "is_required": false,
            "name": "log_level",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"dagster\\"",
            "description": "The name of your logger.",
            "is_required": false,
            "name": "name",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "key",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "limit",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "value",
            "type_key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
          }
        ],
        "given_name": null,
        "key": "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          }
        ],
        "given_name": null,
        "key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
            "is_required": false,
            "name": "io_manager",
            "type_key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7"
          }
        ],
        "given_name": null,
        "key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "applyLimitPerUniqueValue",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "result",
            "type_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742"
          }
        ],
        "given_name": null,
        "key": "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "[DEPRECATED]",
            "is_required": false,
            "name": "marker_to_close",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          }
        ],
        "given_name": null,
        "key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "path",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Explicitly specify the modules to preload in the forkserver. Otherwise, there are two cases for default values if modules are not specified. If the Dagster job was loaded from a module, the same module will be preloaded. If not, the `dagster` module is preloaded.",
            "is_required": false,
            "name": "preload_modules",
            "type_key": "Array.String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.60acefe08e1243b47034a632522b12985eb4acd1": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "0",
            "description": "The number of processes that may run concurrently. By default, this is set to be the return value of `multiprocessing.cpu_count()`.",
            "is_required": false,
            "name": "max_concurrent",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Select how subprocesses are created. By default, `spawn` is selected. See https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods.",
            "is_required": false,
            "name": "start_method",
            "type_key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "A set of limits that are applied to steps with particular tags. If a value is set, the limit is applied to only that key-value pair. If no value is set, the limit is applied across all values of that key. If the value is set to a dict with `applyLimitPerUniqueValue: true`, the limit will apply to the number of unique values for that key. Note that these limits are per run, not global.",
            "is_required": false,
            "name": "tag_concurrency_limits",
            "type_key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
          }
        ],
        "given_name": null,
        "key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.679d0a9f9e9d7f51d5a623c7978ce1b790390fce": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"config\\": {\\"multiprocess\\": {\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}}}",
            "description": "Configure how steps are executed within a run.",
            "is_required": false,
            "name": "execution",
            "type_key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure how loggers emit messages within a run.",
            "is_required": false,
            "name": "loggers",
            "type_key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"noop_op\\": {}}",
            "description": "Configure runtime parameters for ops or assets.",
            "is_required": false,
            "name": "ops",
            "type_key": "Shape.ae8a7d8bfcf3e7bb1e3d8b4e0b8bfb80ce200977"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"io_manager\\": {}}",
            "description": "Configure how shared resources are implemented within a run.",
            "is_required": false,
            "name": "resources",
            "type_key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778"
          }
        ],
        "given_name": null,
        "key": "Shape.679d0a9f9e9d7f51d5a623c7978ce1b790390fce",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.743e47901855cb245064dd633e217bfcb49a11a7": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.ae8a7d8bfcf3e7bb1e3d8b4e0b8bfb80ce200977": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "noop_op",
            "type_key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5"
          }
        ],
        "given_name": null,
        "key": "Shape.ae8a7d8bfcf3e7bb1e3d8b4e0b8bfb80ce200977",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [],
        "given_name": null,
        "key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "outputs",
            "type_key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
          }
        ],
        "given_name": null,
        "key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "console",
            "type_key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a"
          }
        ],
        "given_name": null,
        "key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"multiprocess\\": {}}",
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2"
          }
        ],
        "given_name": null,
        "key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "String": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "String",
        "key": "String",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.STRING"
        },
        "type_param_keys": null
      }
    }
  },
  "dagster_type_namespace_snapshot": {
    "__class__": "DagsterTypeNamespaceSnapshot",
    "all_dagster_type_snaps_by_key": {
      "Any": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Any",
        "is_builtin": true,
        "key": "Any",
        "kind": {
          "__enum__": "DagsterTypeKind.ANY"
        },
        "loader_schema_key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Any",
        "type_param_keys": []
      },
      "Bool": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Bool",
        "is_builtin": true,
        "key": "Bool",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Bool",
        "type_param_keys": []
      },
      "Float": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Float",
        "is_builtin": true,
        "key": "Float",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Float",
        "type_param_keys": []
      },
      "Int": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Int",
        "is_builtin": true,
        "key": "Int",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Int",
        "type_param_keys": []
      },
      "Nothing": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Nothing",
        "is_builtin": true,
        "key": "Nothing",
        "kind": {
          "__enum__": "DagsterTypeKind.NOTHING"
        },
        "loader_schema_key": null,
        "materializer_schema_key": null,
        "name": "Nothing",
        "type_param_keys": []
      },
      "String": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "String",
        "is_builtin": true,
        "key": "String",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "String",
        "type_param_keys": []
      }
    }
  },
  "dep_structure_snapshot": {
    "__class__": "DependencyStructureSnapshot",
    "solid_invocation_snaps": [
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [],
        "is_dynamic_mapped": false,
        "solid_def_name": "noop_op",
        "solid_name": "noop_op",
        "tags": {}
      }
    ]
  },
  "description": null,
  "graph_def_name": "noop_job",
  "lineage_snapshot": null,
  "mode_def_snaps": [
    {
      "__class__": "ModeDefSnap",
      "description": null,
      "logger_def_snaps": [
        {
          "__class__": "LoggerDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          },
          "description": "The default colored console logger.",
          "name": "console"
        }
      ],
      "name": "default",
      "resource_def_snaps": [
        {
          "__class__": "ResourceDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
          "name": "io_manager"
        }
      ],
      "root_config_key": "Shape.679d0a9f9e9d7f51d5a623c7978ce1b790390fce"
    }
  ],
  "name": "noop_job",
  "solid_definitions_snapshot": {
    "__class__": "SolidDefinitionsSnapshot",
    "composite_solid_def_snaps": [],
    "solid_def_snaps": [
      {
        "__class__": "SolidDefSnap",
        "config_field_snap": {
          "__class__": "ConfigFieldSnap",
          "default_provided": false,
          "default_value_as_json_str": null,
          "description": null,
          "is_required": false,
          "name": "config",
          "type_key": "Any"
        },
        "description": null,
        "input_def_snaps": [],
        "name": "noop_op",
        "output_def_snaps": [
          {
            "__class__": "OutputDefSnap",
            "dagster_type_key": "Any",
            "description": null,
            "is_dynamic": false,
            "is_required": true,
            "name": "result"
          }
        ],
        "required_resource_keys": [],
        "tags": {}
      }
    ]
  },
  "tags": {}
}'''

snapshots['test_empty_pipeline_snap_props 2'] = '86087d07c532ad431cd2fda8a2506157d0680933'

snapshots['test_empty_pipeline_snap_snapshot 1'] = '''{
  "__class__": "PipelineSnapshot",
  "config_schema_snapshot": {
    "__class__": "ConfigSchemaSnapshot",
    "all_config_snaps_by_key": {
      "Any": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": "Any",
        "key": "Any",
        "kind": {
          "__enum__": "ConfigTypeKind.ANY"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
        ]
      },
      "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
        ]
      },
      "Array.String": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.String",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.String",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String"
        ]
      },
      "Bool": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Bool",
        "key": "Bool",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.BOOL"
        },
        "type_param_keys": null
      },
      "Float": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Float",
        "key": "Float",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.FLOAT"
        },
        "type_param_keys": null
      },
      "Int": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Int",
        "key": "Int",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.INT"
        },
        "type_param_keys": null
      },
      "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Bool",
          "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59"
        ]
      },
      "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Float",
          "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3"
        ]
      },
      "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Int",
          "Selector.a9799b971d12ace70a2d8803c883c863417d0725"
        ]
      },
      "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Selector.e04723c9d9937e3ab21206435b22247cfbe58269"
        ]
      },
      "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
        ]
      },
      "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute all steps in a single process.",
            "is_required": false,
            "name": "in_process",
            "type_key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute each step in an individual process.",
            "is_required": false,
            "name": "multiprocess",
            "type_key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1"
          }
        ],
        "given_name": null,
        "key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "disabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "enabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `forkserver`.",
            "is_required": false,
            "name": "forkserver",
            "type_key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `spawn`.",
            "is_required": false,
            "name": "spawn",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Int"
          }
        ],
        "given_name": null,
        "key": "Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Float"
          }
        ],
        "given_name": null,
        "key": "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          }
        ],
        "given_name": null,
        "key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.081354663b9d4b8fbfd1cb8e358763912953913f": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"INFO\\"",
            "description": "The logger\'s threshold.",
            "is_required": false,
            "name": "log_level",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"dagster\\"",
            "description": "The name of your logger.",
            "is_required": false,
            "name": "name",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "key",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "limit",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "value",
            "type_key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
          }
        ],
        "given_name": null,
        "key": "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          }
        ],
        "given_name": null,
        "key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
            "is_required": false,
            "name": "io_manager",
            "type_key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7"
          }
        ],
        "given_name": null,
        "key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "applyLimitPerUniqueValue",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "result",
            "type_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742"
          }
        ],
        "given_name": null,
        "key": "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "[DEPRECATED]",
            "is_required": false,
            "name": "marker_to_close",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          }
        ],
        "given_name": null,
        "key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "path",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Explicitly specify the modules to preload in the forkserver. Otherwise, there are two cases for default values if modules are not specified. If the Dagster job was loaded from a module, the same module will be preloaded. If not, the `dagster` module is preloaded.",
            "is_required": false,
            "name": "preload_modules",
            "type_key": "Array.String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.60acefe08e1243b47034a632522b12985eb4acd1": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "0",
            "description": "The number of processes that may run concurrently. By default, this is set to be the return value of `multiprocessing.cpu_count()`.",
            "is_required": false,
            "name": "max_concurrent",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Select how subprocesses are created. By default, `spawn` is selected. See https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods.",
            "is_required": false,
            "name": "start_method",
            "type_key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "A set of limits that are applied to steps with particular tags. If a value is set, the limit is applied to only that key-value pair. If no value is set, the limit is applied across all values of that key. If the value is set to a dict with `applyLimitPerUniqueValue: true`, the limit will apply to the number of unique values for that key. Note that these limits are per run, not global.",
            "is_required": false,
            "name": "tag_concurrency_limits",
            "type_key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
          }
        ],
        "given_name": null,
        "key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.679d0a9f9e9d7f51d5a623c7978ce1b790390fce": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"config\\": {\\"multiprocess\\": {\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}}}",
            "description": "Configure how steps are executed within a run.",
            "is_required": false,
            "name": "execution",
            "type_key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure how loggers emit messages within a run.",
            "is_required": false,
            "name": "loggers",
            "type_key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"noop_op\\": {}}",
            "description": "Configure runtime parameters for ops or assets.",
            "is_required": false,
            "name": "ops",
            "type_key": "Shape.ae8a7d8bfcf3e7bb1e3d8b4e0b8bfb80ce200977"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"io_manager\\": {}}",
            "description": "Configure how shared resources are implemented within a run.",
            "is_required": false,
            "name": "resources",
            "type_key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778"
          }
        ],
        "given_name": null,
        "key": "Shape.679d0a9f9e9d7f51d5a623c7978ce1b790390fce",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.743e47901855cb245064dd633e217bfcb49a11a7": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.ae8a7d8bfcf3e7bb1e3d8b4e0b8bfb80ce200977": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "noop_op",
            "type_key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5"
          }
        ],
        "given_name": null,
        "key": "Shape.ae8a7d8bfcf3e7bb1e3d8b4e0b8bfb80ce200977",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [],
        "given_name": null,
        "key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "outputs",
            "type_key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
          }
        ],
        "given_name": null,
        "key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "console",
            "type_key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a"
          }
        ],
        "given_name": null,
        "key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"multiprocess\\": {}}",
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2"
          }
        ],
        "given_name": null,
        "key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "String": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "String",
        "key": "String",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.STRING"
        },
        "type_param_keys": null
      }
    }
  },
  "dagster_type_namespace_snapshot": {
    "__class__": "DagsterTypeNamespaceSnapshot",
    "all_dagster_type_snaps_by_key": {
      "Any": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Any",
        "is_builtin": true,
        "key": "Any",
        "kind": {
          "__enum__": "DagsterTypeKind.ANY"
        },
        "loader_schema_key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Any",
        "type_param_keys": []
      },
      "Bool": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Bool",
        "is_builtin": true,
        "key": "Bool",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Bool",
        "type_param_keys": []
      },
      "Float": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Float",
        "is_builtin": true,
        "key": "Float",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Float",
        "type_param_keys": []
      },
      "Int": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Int",
        "is_builtin": true,
        "key": "Int",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Int",
        "type_param_keys": []
      },
      "Nothing": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Nothing",
        "is_builtin": true,
        "key": "Nothing",
        "kind": {
          "__enum__": "DagsterTypeKind.NOTHING"
        },
        "loader_schema_key": null,
        "materializer_schema_key": null,
        "name": "Nothing",
        "type_param_keys": []
      },
      "String": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "String",
        "is_builtin": true,
        "key": "String",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "String",
        "type_param_keys": []
      }
    }
  },
  "dep_structure_snapshot": {
    "__class__": "DependencyStructureSnapshot",
    "solid_invocation_snaps": [
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [],
        "is_dynamic_mapped": false,
        "solid_def_name": "noop_op",
        "solid_name": "noop_op",
        "tags": {}
      }
    ]
  },
  "description": null,
  "graph_def_name": "noop_job",
  "lineage_snapshot": null,
  "mode_def_snaps": [
    {
      "__class__": "ModeDefSnap",
      "description": null,
      "logger_def_snaps": [
        {
          "__class__": "LoggerDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          },
          "description": "The default colored console logger.",
          "name": "console"
        }
      ],
      "name": "default",
      "resource_def_snaps": [
        {
          "__class__": "ResourceDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
          "name": "io_manager"
        }
      ],
      "root_config_key": "Shape.679d0a9f9e9d7f51d5a623c7978ce1b790390fce"
    }
  ],
  "name": "noop_job",
  "solid_definitions_snapshot": {
    "__class__": "SolidDefinitionsSnapshot",
    "composite_solid_def_snaps": [],
    "solid_def_snaps": [
      {
        "__class__": "SolidDefSnap",
        "config_field_snap": {
          "__class__": "ConfigFieldSnap",
          "default_provided": false,
          "default_value_as_json_str": null,
          "description": null,
          "is_required": false,
          "name": "config",
          "type_key": "Any"
        },
        "description": null,
        "input_def_snaps": [],
        "name": "noop_op",
        "output_def_snaps": [
          {
            "__class__": "OutputDefSnap",
            "dagster_type_key": "Any",
            "description": null,
            "is_dynamic": false,
            "is_required": true,
            "name": "result"
          }
        ],
        "required_resource_keys": [],
        "tags": {}
      }
    ]
  },
  "tags": {}
}'''

snapshots['test_multi_type_config_array_dict_fields[Permissive] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": "List of Array.Permissive.1f37a068c7c51aba23e9c41475c78eebc4e58471",
  "enum_values": null,
  "fields": null,
  "given_name": null,
  "key": "Array.Permissive.1f37a068c7c51aba23e9c41475c78eebc4e58471",
  "kind": {
    "__enum__": "ConfigTypeKind.ARRAY"
  },
  "scalar_kind": null,
  "type_param_keys": [
    "Permissive.1f37a068c7c51aba23e9c41475c78eebc4e58471"
  ]
}'''

snapshots['test_multi_type_config_array_dict_fields[Selector] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": "List of Array.Selector.1f37a068c7c51aba23e9c41475c78eebc4e58471",
  "enum_values": null,
  "fields": null,
  "given_name": null,
  "key": "Array.Selector.1f37a068c7c51aba23e9c41475c78eebc4e58471",
  "kind": {
    "__enum__": "ConfigTypeKind.ARRAY"
  },
  "scalar_kind": null,
  "type_param_keys": [
    "Selector.1f37a068c7c51aba23e9c41475c78eebc4e58471"
  ]
}'''

snapshots['test_multi_type_config_array_dict_fields[Shape] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": "List of Array.Shape.1f37a068c7c51aba23e9c41475c78eebc4e58471",
  "enum_values": null,
  "fields": null,
  "given_name": null,
  "key": "Array.Shape.1f37a068c7c51aba23e9c41475c78eebc4e58471",
  "kind": {
    "__enum__": "ConfigTypeKind.ARRAY"
  },
  "scalar_kind": null,
  "type_param_keys": [
    "Shape.1f37a068c7c51aba23e9c41475c78eebc4e58471"
  ]
}'''

snapshots['test_multi_type_config_array_map 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": "List of Array.Map.String.Int",
  "enum_values": null,
  "fields": null,
  "given_name": null,
  "key": "Array.Map.String.Int",
  "kind": {
    "__enum__": "ConfigTypeKind.ARRAY"
  },
  "scalar_kind": null,
  "type_param_keys": [
    "Map.String.Int"
  ]
}'''

snapshots['test_multi_type_config_nested_dicts[nested_dict_types0] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": null,
  "enum_values": null,
  "fields": [
    {
      "__class__": "ConfigFieldSnap",
      "default_provided": false,
      "default_value_as_json_str": null,
      "description": null,
      "is_required": true,
      "name": "foo",
      "type_key": "Permissive.c1ae6abf6c3c9e951eeefe4fde820cafc053ee40"
    }
  ],
  "given_name": null,
  "key": "Selector.cb18f2a8fc9fa17668d8f4fd6b44c86c30c56774",
  "kind": {
    "__enum__": "ConfigTypeKind.SELECTOR"
  },
  "scalar_kind": null,
  "type_param_keys": null
}'''

snapshots['test_multi_type_config_nested_dicts[nested_dict_types1] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": null,
  "enum_values": null,
  "fields": [
    {
      "__class__": "ConfigFieldSnap",
      "default_provided": false,
      "default_value_as_json_str": null,
      "description": null,
      "is_required": true,
      "name": "foo",
      "type_key": "Shape.9bbda63934c371bf9be9a1cbb6fff9f5ee0be828"
    }
  ],
  "given_name": null,
  "key": "Selector.b188a7737a2fecf0fca8cf94d331be517176dddf",
  "kind": {
    "__enum__": "ConfigTypeKind.SELECTOR"
  },
  "scalar_kind": null,
  "type_param_keys": null
}'''

snapshots['test_multi_type_config_nested_dicts[nested_dict_types2] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": null,
  "enum_values": null,
  "fields": [
    {
      "__class__": "ConfigFieldSnap",
      "default_provided": false,
      "default_value_as_json_str": null,
      "description": null,
      "is_required": true,
      "name": "foo",
      "type_key": "Selector.c1ae6abf6c3c9e951eeefe4fde820cafc053ee40"
    }
  ],
  "given_name": null,
  "key": "Permissive.84180c8bd71a154af9d2965c8955925c228dc2bf",
  "kind": {
    "__enum__": "ConfigTypeKind.PERMISSIVE_SHAPE"
  },
  "scalar_kind": null,
  "type_param_keys": null
}'''

snapshots['test_multi_type_config_nested_dicts[nested_dict_types3] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": null,
  "enum_values": null,
  "fields": [
    {
      "__class__": "ConfigFieldSnap",
      "default_provided": false,
      "default_value_as_json_str": null,
      "description": null,
      "is_required": true,
      "name": "foo",
      "type_key": "Shape.3d03240a3cdb5557305a2118fb3a059896368dd1"
    }
  ],
  "given_name": null,
  "key": "Permissive.31f842392439e3c949b44f9e0e36bd1ed050a6b5",
  "kind": {
    "__enum__": "ConfigTypeKind.PERMISSIVE_SHAPE"
  },
  "scalar_kind": null,
  "type_param_keys": null
}'''

snapshots['test_multi_type_config_nested_dicts[nested_dict_types4] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": null,
  "enum_values": null,
  "fields": [
    {
      "__class__": "ConfigFieldSnap",
      "default_provided": false,
      "default_value_as_json_str": null,
      "description": null,
      "is_required": true,
      "name": "foo",
      "type_key": "Selector.9bbda63934c371bf9be9a1cbb6fff9f5ee0be828"
    }
  ],
  "given_name": null,
  "key": "Shape.88efc4d6ed14b1d35062d1e50a0227f606049e87",
  "kind": {
    "__enum__": "ConfigTypeKind.STRICT_SHAPE"
  },
  "scalar_kind": null,
  "type_param_keys": null
}'''

snapshots['test_multi_type_config_nested_dicts[nested_dict_types5] 1'] = '''{
  "__class__": "ConfigTypeSnap",
  "description": null,
  "enum_values": null,
  "fields": [
    {
      "__class__": "ConfigFieldSnap",
      "default_provided": false,
      "default_value_as_json_str": null,
      "description": null,
      "is_required": true,
      "name": "foo",
      "type_key": "Permissive.3d03240a3cdb5557305a2118fb3a059896368dd1"
    }
  ],
  "given_name": null,
  "key": "Shape.0117583609bbf6ddcd1b1c9586aca163c454ed9d",
  "kind": {
    "__enum__": "ConfigTypeKind.STRICT_SHAPE"
  },
  "scalar_kind": null,
  "type_param_keys": null
}'''

snapshots['test_pipeline_snap_all_props 1'] = '''{
  "__class__": "PipelineSnapshot",
  "config_schema_snapshot": {
    "__class__": "ConfigSchemaSnapshot",
    "all_config_snaps_by_key": {
      "Any": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": "Any",
        "key": "Any",
        "kind": {
          "__enum__": "ConfigTypeKind.ANY"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
        ]
      },
      "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
        ]
      },
      "Array.String": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.String",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.String",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String"
        ]
      },
      "Bool": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Bool",
        "key": "Bool",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.BOOL"
        },
        "type_param_keys": null
      },
      "Float": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Float",
        "key": "Float",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.FLOAT"
        },
        "type_param_keys": null
      },
      "Int": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Int",
        "key": "Int",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.INT"
        },
        "type_param_keys": null
      },
      "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Bool",
          "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59"
        ]
      },
      "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Float",
          "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3"
        ]
      },
      "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Int",
          "Selector.a9799b971d12ace70a2d8803c883c863417d0725"
        ]
      },
      "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Selector.e04723c9d9937e3ab21206435b22247cfbe58269"
        ]
      },
      "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
        ]
      },
      "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "disabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "enabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.1c1582f52086a27e6bcd0f36726fb599317b651c": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"config\\": {\\"retries\\": {\\"enabled\\": {}}}}",
            "description": null,
            "is_required": false,
            "name": "in_process",
            "type_key": "Shape.09d73f0755bf4752d3f121837669c8660dcf451e"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"config\\": {\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}}",
            "description": null,
            "is_required": false,
            "name": "multiprocess",
            "type_key": "Shape.92756569f6a8d8b0d744106fc51a929583a0419c"
          }
        ],
        "given_name": null,
        "key": "Selector.1c1582f52086a27e6bcd0f36726fb599317b651c",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `forkserver`.",
            "is_required": false,
            "name": "forkserver",
            "type_key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `spawn`.",
            "is_required": false,
            "name": "spawn",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Int"
          }
        ],
        "given_name": null,
        "key": "Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Float"
          }
        ],
        "given_name": null,
        "key": "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          }
        ],
        "given_name": null,
        "key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.081354663b9d4b8fbfd1cb8e358763912953913f": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"INFO\\"",
            "description": "The logger\'s threshold.",
            "is_required": false,
            "name": "log_level",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"dagster\\"",
            "description": "The name of your logger.",
            "is_required": false,
            "name": "name",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.09d73f0755bf4752d3f121837669c8660dcf451e": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute all steps in a single process.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c"
          }
        ],
        "given_name": null,
        "key": "Shape.09d73f0755bf4752d3f121837669c8660dcf451e",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "key",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "limit",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "value",
            "type_key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
          }
        ],
        "given_name": null,
        "key": "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          }
        ],
        "given_name": null,
        "key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.141e902c9a169b052d210da0dc0be0a25615b797": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "solids": "ops"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "noop_op",
            "type_key": "Shape.69ff9be621991cc7961ea5e667d43edaac9d2339"
          }
        ],
        "given_name": null,
        "key": "Shape.141e902c9a169b052d210da0dc0be0a25615b797",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "applyLimitPerUniqueValue",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "result",
            "type_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742"
          }
        ],
        "given_name": null,
        "key": "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "[DEPRECATED]",
            "is_required": false,
            "name": "marker_to_close",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          }
        ],
        "given_name": null,
        "key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "path",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Explicitly specify the modules to preload in the forkserver. Otherwise, there are two cases for default values if modules are not specified. If the Dagster job was loaded from a module, the same module will be preloaded. If not, the `dagster` module is preloaded.",
            "is_required": false,
            "name": "preload_modules",
            "type_key": "Array.String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.60acefe08e1243b47034a632522b12985eb4acd1": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "0",
            "description": "The number of processes that may run concurrently. By default, this is set to be the return value of `multiprocessing.cpu_count()`.",
            "is_required": false,
            "name": "max_concurrent",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Select how subprocesses are created. By default, `spawn` is selected. See https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods.",
            "is_required": false,
            "name": "start_method",
            "type_key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "A set of limits that are applied to steps with particular tags. If a value is set, the limit is applied to only that key-value pair. If no value is set, the limit is applied across all values of that key. If the value is set to a dict with `applyLimitPerUniqueValue: true`, the limit will apply to the number of unique values for that key. Note that these limits are per run, not global.",
            "is_required": false,
            "name": "tag_concurrency_limits",
            "type_key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
          }
        ],
        "given_name": null,
        "key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.69ff9be621991cc7961ea5e667d43edaac9d2339": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "solids": "ops"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "outputs",
            "type_key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
          }
        ],
        "given_name": null,
        "key": "Shape.69ff9be621991cc7961ea5e667d43edaac9d2339",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.743e47901855cb245064dd633e217bfcb49a11a7": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.92756569f6a8d8b0d744106fc51a929583a0419c": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute each step in an individual process.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1"
          }
        ],
        "given_name": null,
        "key": "Shape.92756569f6a8d8b0d744106fc51a929583a0419c",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.95e096750f330490a26714025addb5f403b099e6": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Built-in IO manager that stores and retrieves values in memory.",
            "is_required": false,
            "name": "io_manager",
            "type_key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7"
          }
        ],
        "given_name": null,
        "key": "Shape.95e096750f330490a26714025addb5f403b099e6",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [],
        "given_name": null,
        "key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e83ae477fb3d5c95e531a8f7cc8dbd38a5e149c0": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "solids": "ops"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"in_process\\": {}}",
            "description": "Configure how steps are executed within a run.",
            "is_required": false,
            "name": "execution",
            "type_key": "Selector.1c1582f52086a27e6bcd0f36726fb599317b651c"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure how loggers emit messages within a run.",
            "is_required": false,
            "name": "loggers",
            "type_key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"io_manager\\": {}}",
            "description": "Configure how shared resources are implemented within a run.",
            "is_required": false,
            "name": "resources",
            "type_key": "Shape.95e096750f330490a26714025addb5f403b099e6"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"noop_op\\": {}}",
            "description": "Configure runtime parameters for ops or assets.",
            "is_required": false,
            "name": "solids",
            "type_key": "Shape.141e902c9a169b052d210da0dc0be0a25615b797"
          }
        ],
        "given_name": null,
        "key": "Shape.e83ae477fb3d5c95e531a8f7cc8dbd38a5e149c0",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "console",
            "type_key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a"
          }
        ],
        "given_name": null,
        "key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "String": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "String",
        "key": "String",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.STRING"
        },
        "type_param_keys": null
      }
    }
  },
  "dagster_type_namespace_snapshot": {
    "__class__": "DagsterTypeNamespaceSnapshot",
    "all_dagster_type_snaps_by_key": {
      "Any": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Any",
        "is_builtin": true,
        "key": "Any",
        "kind": {
          "__enum__": "DagsterTypeKind.ANY"
        },
        "loader_schema_key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Any",
        "type_param_keys": []
      },
      "Bool": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Bool",
        "is_builtin": true,
        "key": "Bool",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Bool",
        "type_param_keys": []
      },
      "Float": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Float",
        "is_builtin": true,
        "key": "Float",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Float",
        "type_param_keys": []
      },
      "Int": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Int",
        "is_builtin": true,
        "key": "Int",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Int",
        "type_param_keys": []
      },
      "Nothing": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Nothing",
        "is_builtin": true,
        "key": "Nothing",
        "kind": {
          "__enum__": "DagsterTypeKind.NOTHING"
        },
        "loader_schema_key": null,
        "materializer_schema_key": null,
        "name": "Nothing",
        "type_param_keys": []
      },
      "String": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "String",
        "is_builtin": true,
        "key": "String",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "String",
        "type_param_keys": []
      }
    }
  },
  "dep_structure_snapshot": {
    "__class__": "DependencyStructureSnapshot",
    "solid_invocation_snaps": [
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [],
        "is_dynamic_mapped": false,
        "solid_def_name": "noop_op",
        "solid_name": "noop_op",
        "tags": {}
      }
    ]
  },
  "description": "desc",
  "graph_def_name": "noop_job",
  "lineage_snapshot": null,
  "mode_def_snaps": [
    {
      "__class__": "ModeDefSnap",
      "description": null,
      "logger_def_snaps": [
        {
          "__class__": "LoggerDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          },
          "description": "The default colored console logger.",
          "name": "console"
        }
      ],
      "name": "default",
      "resource_def_snaps": [
        {
          "__class__": "ResourceDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          "description": "Built-in IO manager that stores and retrieves values in memory.",
          "name": "io_manager"
        }
      ],
      "root_config_key": "Shape.e83ae477fb3d5c95e531a8f7cc8dbd38a5e149c0"
    }
  ],
  "name": "noop_job",
  "solid_definitions_snapshot": {
    "__class__": "SolidDefinitionsSnapshot",
    "composite_solid_def_snaps": [],
    "solid_def_snaps": [
      {
        "__class__": "SolidDefSnap",
        "config_field_snap": {
          "__class__": "ConfigFieldSnap",
          "default_provided": false,
          "default_value_as_json_str": null,
          "description": null,
          "is_required": false,
          "name": "config",
          "type_key": "Any"
        },
        "description": null,
        "input_def_snaps": [],
        "name": "noop_op",
        "output_def_snaps": [
          {
            "__class__": "OutputDefSnap",
            "dagster_type_key": "Any",
            "description": null,
            "is_dynamic": false,
            "is_required": true,
            "name": "result"
          }
        ],
        "required_resource_keys": [],
        "tags": {}
      }
    ]
  },
  "tags": {
    "key": "value"
  }
}'''

snapshots['test_pipeline_snap_all_props 2'] = '2856fe52d120063caa908c7179ee4f693688a215'

snapshots['test_two_invocations_deps_snap 1'] = '''{
  "__class__": "PipelineSnapshot",
  "config_schema_snapshot": {
    "__class__": "ConfigSchemaSnapshot",
    "all_config_snaps_by_key": {
      "Any": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": "Any",
        "key": "Any",
        "kind": {
          "__enum__": "ConfigTypeKind.ANY"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
        ]
      },
      "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
        ]
      },
      "Array.String": {
        "__class__": "ConfigTypeSnap",
        "description": "List of Array.String",
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "Array.String",
        "kind": {
          "__enum__": "ConfigTypeKind.ARRAY"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String"
        ]
      },
      "Bool": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Bool",
        "key": "Bool",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.BOOL"
        },
        "type_param_keys": null
      },
      "Float": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Float",
        "key": "Float",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.FLOAT"
        },
        "type_param_keys": null
      },
      "Int": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "Int",
        "key": "Int",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.INT"
        },
        "type_param_keys": null
      },
      "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Bool",
          "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59"
        ]
      },
      "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Float",
          "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3"
        ]
      },
      "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "Int",
          "Selector.a9799b971d12ace70a2d8803c883c863417d0725"
        ]
      },
      "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Selector.e04723c9d9937e3ab21206435b22247cfbe58269"
        ]
      },
      "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": null,
        "given_name": null,
        "key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR_UNION"
        },
        "scalar_kind": null,
        "type_param_keys": [
          "String",
          "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
        ]
      },
      "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute all steps in a single process.",
            "is_required": false,
            "name": "in_process",
            "type_key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}",
            "description": "Execute each step in an individual process.",
            "is_required": false,
            "name": "multiprocess",
            "type_key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1"
          }
        ],
        "given_name": null,
        "key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "disabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "enabled",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `forkserver`.",
            "is_required": false,
            "name": "forkserver",
            "type_key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure the multiprocess executor to start subprocesses using `spawn`.",
            "is_required": false,
            "name": "spawn",
            "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
          }
        ],
        "given_name": null,
        "key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Int"
          }
        ],
        "given_name": null,
        "key": "Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Float"
          }
        ],
        "given_name": null,
        "key": "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          }
        ],
        "given_name": null,
        "key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "json",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "pickle",
            "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "value",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "kind": {
          "__enum__": "ConfigTypeKind.SELECTOR"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.081354663b9d4b8fbfd1cb8e358763912953913f": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"INFO\\"",
            "description": "The logger\'s threshold.",
            "is_required": false,
            "name": "log_level",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "\\"dagster\\"",
            "description": "The name of your logger.",
            "is_required": false,
            "name": "name",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "key",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "limit",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "value",
            "type_key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
          }
        ],
        "given_name": null,
        "key": "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          }
        ],
        "given_name": null,
        "key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
            "is_required": false,
            "name": "io_manager",
            "type_key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7"
          }
        ],
        "given_name": null,
        "key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "applyLimitPerUniqueValue",
            "type_key": "Bool"
          }
        ],
        "given_name": null,
        "key": "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "result",
            "type_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742"
          }
        ],
        "given_name": null,
        "key": "Shape.41de0e2d7b75524510155d0bdab8723c6feced3b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "[DEPRECATED]",
            "is_required": false,
            "name": "marker_to_close",
            "type_key": "String"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          }
        ],
        "given_name": null,
        "key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": true,
            "name": "path",
            "type_key": "String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Explicitly specify the modules to preload in the forkserver. Otherwise, there are two cases for default values if modules are not specified. If the Dagster job was loaded from a module, the same module will be preloaded. If not, the `dagster` module is preloaded.",
            "is_required": false,
            "name": "preload_modules",
            "type_key": "Array.String"
          }
        ],
        "given_name": null,
        "key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.60acefe08e1243b47034a632522b12985eb4acd1": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "0",
            "description": "The number of processes that may run concurrently. By default, this is set to be the return value of `multiprocessing.cpu_count()`.",
            "is_required": false,
            "name": "max_concurrent",
            "type_key": "Int"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"enabled\\": {}}",
            "description": "Whether retries are enabled or not. By default, retries are enabled.",
            "is_required": false,
            "name": "retries",
            "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "Select how subprocesses are created. By default, `spawn` is selected. See https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods.",
            "is_required": false,
            "name": "start_method",
            "type_key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": "A set of limits that are applied to steps with particular tags. If a value is set, the limit is applied to only that key-value pair. If no value is set, the limit is applied across all values of that key. If the value is set to a dict with `applyLimitPerUniqueValue: true`, the limit will apply to the number of unique values for that key. Note that these limits are per run, not global.",
            "is_required": false,
            "name": "tag_concurrency_limits",
            "type_key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
          }
        ],
        "given_name": null,
        "key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.743e47901855cb245064dd633e217bfcb49a11a7": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          }
        ],
        "given_name": null,
        "key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.a689db92b1e7b14e3941e9ce057aff916ad79101": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"config\\": {\\"multiprocess\\": {\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}}}",
            "description": "Configure how steps are executed within a run.",
            "is_required": false,
            "name": "execution",
            "type_key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": "Configure how loggers emit messages within a run.",
            "is_required": false,
            "name": "loggers",
            "type_key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"one\\": {}, \\"two\\": {}}",
            "description": "Configure runtime parameters for ops or assets.",
            "is_required": false,
            "name": "ops",
            "type_key": "Shape.c854c5726a119f028b72c37e7f358eaa7564dc59"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"io_manager\\": {}}",
            "description": "Configure how shared resources are implemented within a run.",
            "is_required": false,
            "name": "resources",
            "type_key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778"
          }
        ],
        "given_name": null,
        "key": "Shape.a689db92b1e7b14e3941e9ce057aff916ad79101",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.c854c5726a119f028b72c37e7f358eaa7564dc59": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "one",
            "type_key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{}",
            "description": null,
            "is_required": false,
            "name": "two",
            "type_key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5"
          }
        ],
        "given_name": null,
        "key": "Shape.c854c5726a119f028b72c37e7f358eaa7564dc59",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [],
        "given_name": null,
        "key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "field_aliases": {
          "ops": "solids"
        },
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "outputs",
            "type_key": "Array.Shape.41de0e2d7b75524510155d0bdab8723c6feced3b"
          }
        ],
        "given_name": null,
        "key": "Shape.e20183fcf9f186a6569b322579dcc1e6fae8d0d5",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "console",
            "type_key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a"
          }
        ],
        "given_name": null,
        "key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b": {
        "__class__": "ConfigTypeSnap",
        "description": null,
        "enum_values": null,
        "fields": [
          {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"multiprocess\\": {}}",
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2"
          }
        ],
        "given_name": null,
        "key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b",
        "kind": {
          "__enum__": "ConfigTypeKind.STRICT_SHAPE"
        },
        "scalar_kind": null,
        "type_param_keys": null
      },
      "String": {
        "__class__": "ConfigTypeSnap",
        "description": "",
        "enum_values": null,
        "fields": null,
        "given_name": "String",
        "key": "String",
        "kind": {
          "__enum__": "ConfigTypeKind.SCALAR"
        },
        "scalar_kind": {
          "__enum__": "ConfigScalarKind.STRING"
        },
        "type_param_keys": null
      }
    }
  },
  "dagster_type_namespace_snapshot": {
    "__class__": "DagsterTypeNamespaceSnapshot",
    "all_dagster_type_snaps_by_key": {
      "Any": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Any",
        "is_builtin": true,
        "key": "Any",
        "kind": {
          "__enum__": "DagsterTypeKind.ANY"
        },
        "loader_schema_key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Any",
        "type_param_keys": []
      },
      "Bool": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Bool",
        "is_builtin": true,
        "key": "Bool",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Bool",
        "type_param_keys": []
      },
      "Float": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Float",
        "is_builtin": true,
        "key": "Float",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Float",
        "type_param_keys": []
      },
      "Int": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Int",
        "is_builtin": true,
        "key": "Int",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "Int",
        "type_param_keys": []
      },
      "Nothing": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "Nothing",
        "is_builtin": true,
        "key": "Nothing",
        "kind": {
          "__enum__": "DagsterTypeKind.NOTHING"
        },
        "loader_schema_key": null,
        "materializer_schema_key": null,
        "name": "Nothing",
        "type_param_keys": []
      },
      "String": {
        "__class__": "DagsterTypeSnap",
        "description": null,
        "display_name": "String",
        "is_builtin": true,
        "key": "String",
        "kind": {
          "__enum__": "DagsterTypeKind.SCALAR"
        },
        "loader_schema_key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
        "materializer_schema_key": "Selector.e52fa3afbe531d9522fae1206f3ae9d248775742",
        "name": "String",
        "type_param_keys": []
      }
    }
  },
  "dep_structure_snapshot": {
    "__class__": "DependencyStructureSnapshot",
    "solid_invocation_snaps": [
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [],
        "is_dynamic_mapped": false,
        "solid_def_name": "noop_op",
        "solid_name": "one",
        "tags": {}
      },
      {
        "__class__": "SolidInvocationSnap",
        "input_dep_snaps": [],
        "is_dynamic_mapped": false,
        "solid_def_name": "noop_op",
        "solid_name": "two",
        "tags": {}
      }
    ]
  },
  "description": null,
  "graph_def_name": "two_solid_job",
  "lineage_snapshot": null,
  "mode_def_snaps": [
    {
      "__class__": "ModeDefSnap",
      "description": null,
      "logger_def_snaps": [
        {
          "__class__": "LoggerDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": true,
            "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
            "description": "The default colored console logger.",
            "is_required": false,
            "name": "config",
            "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
          },
          "description": "The default colored console logger.",
          "name": "console"
        }
      ],
      "name": "default",
      "resource_def_snaps": [
        {
          "__class__": "ResourceDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
          "name": "io_manager"
        }
      ],
      "root_config_key": "Shape.a689db92b1e7b14e3941e9ce057aff916ad79101"
    }
  ],
  "name": "two_solid_job",
  "solid_definitions_snapshot": {
    "__class__": "SolidDefinitionsSnapshot",
    "composite_solid_def_snaps": [],
    "solid_def_snaps": [
      {
        "__class__": "SolidDefSnap",
        "config_field_snap": {
          "__class__": "ConfigFieldSnap",
          "default_provided": false,
          "default_value_as_json_str": null,
          "description": null,
          "is_required": false,
          "name": "config",
          "type_key": "Any"
        },
        "description": null,
        "input_def_snaps": [],
        "name": "noop_op",
        "output_def_snaps": [
          {
            "__class__": "OutputDefSnap",
            "dagster_type_key": "Any",
            "description": null,
            "is_dynamic": false,
            "is_required": true,
            "name": "result"
          }
        ],
        "required_resource_keys": [],
        "tags": {}
      }
    ]
  },
  "tags": {}
}'''

snapshots['test_two_invocations_deps_snap 2'] = '1dc05eb380211786de36a304548d451783bb3edf'
