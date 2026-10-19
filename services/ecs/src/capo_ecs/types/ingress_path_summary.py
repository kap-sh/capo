"""Generated from Smithy shape ``com.amazonaws.ecs#IngressPathSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.access_type
    import capo_ecs.types.string


class IngressPathSummary(TypedDict, closed=True):
    access_type: "capo_ecs.types.access_type.AccessType"
    """<p>The type of access to the endpoint for the Express service.</p>"""
    endpoint: "capo_ecs.types.string.String"
    """<p>The endpoint for access to the service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngressPathSummary) -> dict:
    out: dict = {}
    import capo_ecs.types.access_type

    out["accessType"] = capo_ecs.types.access_type.serialize_aws_json_1_1(
        value["access_type"]
    )
    out["endpoint"] = value["endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IngressPathSummary:
    out: IngressPathSummary = {}  # type: ignore[typeddict-item]
    if data.get("accessType") is not None:
        import capo_ecs.types.access_type

        out["access_type"] = capo_ecs.types.access_type.deserialize_aws_json_1_1(
            data["accessType"]
        )
    else:
        import typing

        out["access_type"] = typing.cast("capo_ecs.types.access_type.AccessType", "")
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    return out
