.. _api_file_flyteidl/admin/matchable_resource.proto:

matchable_resource.proto
=======================================

.. _api_msg_flyteidl.admin.TaskResourceSpec:

flyteidl.admin.TaskResourceSpec
-------------------------------

`[flyteidl.admin.TaskResourceSpec proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L30>`_


.. code-block:: json

  {
    "cpu": "...",
    "gpu": "...",
    "memory": "...",
    "storage": "..."
  }

.. _api_field_flyteidl.admin.TaskResourceSpec.cpu:

cpu
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyteidl.admin.TaskResourceSpec.gpu:

gpu
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyteidl.admin.TaskResourceSpec.memory:

memory
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyteidl.admin.TaskResourceSpec.storage:

storage
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  


.. _api_msg_flyteidl.admin.TaskResourceAttributes:

flyteidl.admin.TaskResourceAttributes
-------------------------------------

`[flyteidl.admin.TaskResourceAttributes proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L40>`_


.. code-block:: json

  {
    "defaults": "{...}",
    "limits": "{...}"
  }

.. _api_field_flyteidl.admin.TaskResourceAttributes.defaults:

defaults
  (:ref:`flyteidl.admin.TaskResourceSpec <api_msg_flyteidl.admin.TaskResourceSpec>`) 
  
.. _api_field_flyteidl.admin.TaskResourceAttributes.limits:

limits
  (:ref:`flyteidl.admin.TaskResourceSpec <api_msg_flyteidl.admin.TaskResourceSpec>`) 
  


.. _api_msg_flyteidl.admin.ClusterResourceAttributes:

flyteidl.admin.ClusterResourceAttributes
----------------------------------------

`[flyteidl.admin.ClusterResourceAttributes proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L46>`_


.. code-block:: json

  {
    "attributes": "{...}"
  }

.. _api_field_flyteidl.admin.ClusterResourceAttributes.attributes:

attributes
  (map<`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_, `string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_>) Custom resource attributes which will be applied in cluster resource creation (e.g. quotas).
  Map keys are the *case-sensitive* names of variables in templatized resource files.
  Map values should be the custom values which get substituted during resource creation.
  
  


.. _api_msg_flyteidl.admin.ExecutionQueueAttributes:

flyteidl.admin.ExecutionQueueAttributes
---------------------------------------

`[flyteidl.admin.ExecutionQueueAttributes proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L53>`_


.. code-block:: json

  {
    "tags": []
  }

.. _api_field_flyteidl.admin.ExecutionQueueAttributes.tags:

tags
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) Tags used for assigning execution queues for tasks defined within this project.
  
  


.. _api_msg_flyteidl.admin.ExecutionClusterLabel:

flyteidl.admin.ExecutionClusterLabel
------------------------------------

`[flyteidl.admin.ExecutionClusterLabel proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L58>`_


.. code-block:: json

  {
    "value": "..."
  }

.. _api_field_flyteidl.admin.ExecutionClusterLabel.value:

value
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) Label value to determine where the execution will be run
  
  


.. _api_msg_flyteidl.admin.PluginOverride:

flyteidl.admin.PluginOverride
-----------------------------

`[flyteidl.admin.PluginOverride proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L63>`_


.. code-block:: json

  {
    "task_type": "...",
    "plugin_id": "...",
    "fallback_plugin_ids": [],
    "missing_plugin_behavior": "..."
  }

.. _api_field_flyteidl.admin.PluginOverride.task_type:

task_type
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) A predefined yet extensible Task type identifier.
  
  
.. _api_field_flyteidl.admin.PluginOverride.plugin_id:

plugin_id
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) The unique name of the plugin which should handle tasks of this type instead of the default registered plugin.
  
  
.. _api_field_flyteidl.admin.PluginOverride.fallback_plugin_ids:

fallback_plugin_ids
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) OPTIONAL The unique names of the plugin implementations, in order of decreasing preference, which should handle tasks of this type when the override plugin id is unavailable on the flyte platform.
  
  
.. _api_field_flyteidl.admin.PluginOverride.missing_plugin_behavior:

missing_plugin_behavior
  (:ref:`flyteidl.admin.PluginOverride.MissingPluginBehavior <api_enum_flyteidl.admin.PluginOverride.MissingPluginBehavior>`) 
  

.. _api_enum_flyteidl.admin.PluginOverride.MissingPluginBehavior:

Enum flyteidl.admin.PluginOverride.MissingPluginBehavior
--------------------------------------------------------

`[flyteidl.admin.PluginOverride.MissingPluginBehavior proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L73>`_


.. _api_enum_value_flyteidl.admin.PluginOverride.MissingPluginBehavior.FAIL:

FAIL
  *(DEFAULT)* ⁣
  
.. _api_enum_value_flyteidl.admin.PluginOverride.MissingPluginBehavior.OVERRIDE_FALLBACK:

OVERRIDE_FALLBACK
  ⁣Use the in-order list of fallback_plugin_ids as supported fallbacks for this task type.
  
  
.. _api_enum_value_flyteidl.admin.PluginOverride.MissingPluginBehavior.USE_DEFAULT:

USE_DEFAULT
  ⁣Uses the system-configured default implementation.
  
  

.. _api_msg_flyteidl.admin.MatchingAttributes:

flyteidl.admin.MatchingAttributes
---------------------------------

`[flyteidl.admin.MatchingAttributes proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L87>`_

Generic container for encapsulating all types of the above attributes messages.

.. code-block:: json

  {
    "task_resource_attributes": "{...}",
    "cluster_resource_attributes": "{...}",
    "execution_queue_attributes": "{...}",
    "execution_cluster_label": "{...}",
    "quality_of_service": "{...}",
    "plugin_override": "{...}"
  }

.. _api_field_flyteidl.admin.MatchingAttributes.task_resource_attributes:

task_resource_attributes
  (:ref:`flyteidl.admin.TaskResourceAttributes <api_msg_flyteidl.admin.TaskResourceAttributes>`) 
  
  
  Only one of :ref:`task_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.task_resource_attributes>`, :ref:`cluster_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.cluster_resource_attributes>`, :ref:`execution_queue_attributes <api_field_flyteidl.admin.MatchingAttributes.execution_queue_attributes>`, :ref:`execution_cluster_label <api_field_flyteidl.admin.MatchingAttributes.execution_cluster_label>`, :ref:`quality_of_service <api_field_flyteidl.admin.MatchingAttributes.quality_of_service>`, :ref:`plugin_override <api_field_flyteidl.admin.MatchingAttributes.plugin_override>` may be set.
  
.. _api_field_flyteidl.admin.MatchingAttributes.cluster_resource_attributes:

cluster_resource_attributes
  (:ref:`flyteidl.admin.ClusterResourceAttributes <api_msg_flyteidl.admin.ClusterResourceAttributes>`) 
  
  
  Only one of :ref:`task_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.task_resource_attributes>`, :ref:`cluster_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.cluster_resource_attributes>`, :ref:`execution_queue_attributes <api_field_flyteidl.admin.MatchingAttributes.execution_queue_attributes>`, :ref:`execution_cluster_label <api_field_flyteidl.admin.MatchingAttributes.execution_cluster_label>`, :ref:`quality_of_service <api_field_flyteidl.admin.MatchingAttributes.quality_of_service>`, :ref:`plugin_override <api_field_flyteidl.admin.MatchingAttributes.plugin_override>` may be set.
  
.. _api_field_flyteidl.admin.MatchingAttributes.execution_queue_attributes:

execution_queue_attributes
  (:ref:`flyteidl.admin.ExecutionQueueAttributes <api_msg_flyteidl.admin.ExecutionQueueAttributes>`) 
  
  
  Only one of :ref:`task_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.task_resource_attributes>`, :ref:`cluster_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.cluster_resource_attributes>`, :ref:`execution_queue_attributes <api_field_flyteidl.admin.MatchingAttributes.execution_queue_attributes>`, :ref:`execution_cluster_label <api_field_flyteidl.admin.MatchingAttributes.execution_cluster_label>`, :ref:`quality_of_service <api_field_flyteidl.admin.MatchingAttributes.quality_of_service>`, :ref:`plugin_override <api_field_flyteidl.admin.MatchingAttributes.plugin_override>` may be set.
  
.. _api_field_flyteidl.admin.MatchingAttributes.execution_cluster_label:

execution_cluster_label
  (:ref:`flyteidl.admin.ExecutionClusterLabel <api_msg_flyteidl.admin.ExecutionClusterLabel>`) 
  
  
  Only one of :ref:`task_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.task_resource_attributes>`, :ref:`cluster_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.cluster_resource_attributes>`, :ref:`execution_queue_attributes <api_field_flyteidl.admin.MatchingAttributes.execution_queue_attributes>`, :ref:`execution_cluster_label <api_field_flyteidl.admin.MatchingAttributes.execution_cluster_label>`, :ref:`quality_of_service <api_field_flyteidl.admin.MatchingAttributes.quality_of_service>`, :ref:`plugin_override <api_field_flyteidl.admin.MatchingAttributes.plugin_override>` may be set.
  
.. _api_field_flyteidl.admin.MatchingAttributes.quality_of_service:

quality_of_service
  (:ref:`flyteidl.core.QualityOfService <api_msg_flyteidl.core.QualityOfService>`) 
  
  
  Only one of :ref:`task_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.task_resource_attributes>`, :ref:`cluster_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.cluster_resource_attributes>`, :ref:`execution_queue_attributes <api_field_flyteidl.admin.MatchingAttributes.execution_queue_attributes>`, :ref:`execution_cluster_label <api_field_flyteidl.admin.MatchingAttributes.execution_cluster_label>`, :ref:`quality_of_service <api_field_flyteidl.admin.MatchingAttributes.quality_of_service>`, :ref:`plugin_override <api_field_flyteidl.admin.MatchingAttributes.plugin_override>` may be set.
  
.. _api_field_flyteidl.admin.MatchingAttributes.plugin_override:

plugin_override
  (:ref:`flyteidl.admin.PluginOverride <api_msg_flyteidl.admin.PluginOverride>`) 
  
  
  Only one of :ref:`task_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.task_resource_attributes>`, :ref:`cluster_resource_attributes <api_field_flyteidl.admin.MatchingAttributes.cluster_resource_attributes>`, :ref:`execution_queue_attributes <api_field_flyteidl.admin.MatchingAttributes.execution_queue_attributes>`, :ref:`execution_cluster_label <api_field_flyteidl.admin.MatchingAttributes.execution_cluster_label>`, :ref:`quality_of_service <api_field_flyteidl.admin.MatchingAttributes.quality_of_service>`, :ref:`plugin_override <api_field_flyteidl.admin.MatchingAttributes.plugin_override>` may be set.
  


.. _api_msg_flyteidl.admin.MatchableAttributesConfiguration:

flyteidl.admin.MatchableAttributesConfiguration
-----------------------------------------------

`[flyteidl.admin.MatchableAttributesConfiguration proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L105>`_

Represents a custom set of attributes applied for either a domain; a domain and project; or
domain, project and workflow name.

.. code-block:: json

  {
    "attributes": "{...}",
    "domain": "...",
    "project": "...",
    "workflow": "...",
    "launch_plan": "..."
  }

.. _api_field_flyteidl.admin.MatchableAttributesConfiguration.attributes:

attributes
  (:ref:`flyteidl.admin.MatchingAttributes <api_msg_flyteidl.admin.MatchingAttributes>`) 
  
.. _api_field_flyteidl.admin.MatchableAttributesConfiguration.domain:

domain
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyteidl.admin.MatchableAttributesConfiguration.project:

project
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyteidl.admin.MatchableAttributesConfiguration.workflow:

workflow
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyteidl.admin.MatchableAttributesConfiguration.launch_plan:

launch_plan
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  


.. _api_msg_flyteidl.admin.ListMatchableAttributesRequest:

flyteidl.admin.ListMatchableAttributesRequest
---------------------------------------------

`[flyteidl.admin.ListMatchableAttributesRequest proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L118>`_

Request all matching resource attributes.

.. code-block:: json

  {
    "resource_type": "..."
  }

.. _api_field_flyteidl.admin.ListMatchableAttributesRequest.resource_type:

resource_type
  (:ref:`flyteidl.admin.MatchableResource <api_enum_flyteidl.admin.MatchableResource>`) 
  


.. _api_msg_flyteidl.admin.ListMatchableAttributesResponse:

flyteidl.admin.ListMatchableAttributesResponse
----------------------------------------------

`[flyteidl.admin.ListMatchableAttributesResponse proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L123>`_

Response for a request for all matching resource attributes.

.. code-block:: json

  {
    "configurations": []
  }

.. _api_field_flyteidl.admin.ListMatchableAttributesResponse.configurations:

configurations
  (:ref:`flyteidl.admin.MatchableAttributesConfiguration <api_msg_flyteidl.admin.MatchableAttributesConfiguration>`) 
  

.. _api_enum_flyteidl.admin.MatchableResource:

Enum flyteidl.admin.MatchableResource
-------------------------------------

`[flyteidl.admin.MatchableResource proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/matchable_resource.proto#L10>`_

Defines a resource that can be configured by customizable Project-, ProjectDomain- or WorkflowAttributes
based on matching tags.

.. _api_enum_value_flyteidl.admin.MatchableResource.TASK_RESOURCE:

TASK_RESOURCE
  *(DEFAULT)* ⁣Applies to customizable task resource requests and limits.
  
  
.. _api_enum_value_flyteidl.admin.MatchableResource.CLUSTER_RESOURCE:

CLUSTER_RESOURCE
  ⁣Applies to configuring templated kubernetes cluster resources.
  
  
.. _api_enum_value_flyteidl.admin.MatchableResource.EXECUTION_QUEUE:

EXECUTION_QUEUE
  ⁣Configures task and dynamic task execution queue assignment.
  
  
.. _api_enum_value_flyteidl.admin.MatchableResource.EXECUTION_CLUSTER_LABEL:

EXECUTION_CLUSTER_LABEL
  ⁣Configures the K8s cluster label to be used for execution to be run
  
  
.. _api_enum_value_flyteidl.admin.MatchableResource.QUALITY_OF_SERVICE_SPECIFICATION:

QUALITY_OF_SERVICE_SPECIFICATION
  ⁣Configures default quality of service when undefined in an execution spec.
  
  
.. _api_enum_value_flyteidl.admin.MatchableResource.PLUGIN_OVERRIDE:

PLUGIN_OVERRIDE
  ⁣Selects configurable plugin implementation behavior for a given task type.
  
  
