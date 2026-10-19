"""Generated from Smithy shape ``com.amazonaws.interconnect#AttachPointDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.attach_point_type


class AttachPointDescriptor(TypedDict, closed=True):
    type: "capo_interconnect.types.attach_point_type.AttachPointType"
    """<p>The type of this AttachPoint, which will dictate the syntax of the identifier.</p> <p>Current types include:</p> <ul> <li> <p>ARN</p> </li> <li> <p>DirectConnect Gateway</p> </li> </ul>"""
    identifier: "str"
    """<p>The identifier for the specific type of the AttachPoint.</p>"""
    name: "str"
    """<p>The descriptive name of the identifier attach point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachPointDescriptor) -> dict:
    out: dict = {}
    import capo_interconnect.types.attach_point_type

    out["type"] = capo_interconnect.types.attach_point_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["identifier"] = value["identifier"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AttachPointDescriptor:
    out: AttachPointDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_interconnect.types.attach_point_type

        out["type"] = (
            capo_interconnect.types.attach_point_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_interconnect.types.attach_point_type.AttachPointType", ""
        )
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
