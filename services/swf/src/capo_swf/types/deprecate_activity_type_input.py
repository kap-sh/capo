"""Generated from Smithy shape ``com.amazonaws.swf#DeprecateActivityTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.activity_type
    import capo_swf.types.domain_name


class DeprecateActivityTypeInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain in which the activity type is registered.</p>"""
    activity_type: "capo_swf.types.activity_type.ActivityType"
    """<p>The activity type to deprecate.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeprecateActivityTypeInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_swf.types.activity_type

    out["activityType"] = capo_swf.types.activity_type.serialize_aws_json_1_0(
        value["activity_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeprecateActivityTypeInput:
    out: DeprecateActivityTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("activityType") is not None:
        import capo_swf.types.activity_type

        out["activity_type"] = capo_swf.types.activity_type.deserialize_aws_json_1_0(
            data["activityType"]
        )
    else:
        raise DeserializationError("DeprecateActivityTypeInput.activity_type required")
    return out
