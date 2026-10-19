"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#EnvironmentProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.property_groups


class EnvironmentProperties(TypedDict, closed=True):
    property_groups: "capo_kinesis_analytics_v2.types.property_groups.PropertyGroups"
    """<p>Describes the execution property groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentProperties) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.property_groups

    out["PropertyGroups"] = (
        capo_kinesis_analytics_v2.types.property_groups.serialize_aws_json_1_1(
            value["property_groups"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentProperties:
    out: EnvironmentProperties = {}  # type: ignore[typeddict-item]
    if data.get("PropertyGroups") is not None:
        import capo_kinesis_analytics_v2.types.property_groups

        out["property_groups"] = (
            capo_kinesis_analytics_v2.types.property_groups.deserialize_aws_json_1_1(
                data["PropertyGroups"]
            )
        )
    else:
        out["property_groups"] = []
    return out
