"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRouterRoutingPreference``."""

from typing import Literal, TypeAlias, cast

"""<p>How an inference router chooses among the destinations of a routing target.</p>"""
InferenceRouterRoutingPreference: TypeAlias = Literal[
    "LocalRegionFirst",
    "InstancePoolOrder",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRouterRoutingPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceRouterRoutingPreference:
    return cast(InferenceRouterRoutingPreference, data)
