"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOnDrainTimeout``."""

from typing import Literal, TypeAlias, cast

"""<p>The action to take if the pods on an instance don't drain within the configured timeout. Valid values are <code>Skip</code> and <code>Force</code>.</p>"""
ClusterOnDrainTimeout: TypeAlias = Literal[
    "Force",
    "Skip",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOnDrainTimeout) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterOnDrainTimeout:
    return cast(ClusterOnDrainTimeout, data)
