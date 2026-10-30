"""Generated from Smithy shape ``com.amazonaws.continuum#ConfigRecorderArn``."""

from typing import TypeAlias

"""ARN of the AWS Config Recorder provisioned by this Collector. Accepts both recorder shapes: - Customer-Managed: ...:config-recorder/{name} - Service-Linked: ...:configuration-recorder/{name}/{id} (a service-linked recorder ARN from PutServiceLinkedConfigurationRecorder uses the `configuration-recorder` resource type and carries a trailing id segment)."""
ConfigRecorderArn: TypeAlias = str
