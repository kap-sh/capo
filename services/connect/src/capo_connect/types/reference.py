"""Generated from Smithy shape ``com.amazonaws.connect#Reference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.reference_arn
    import capo_connect.types.reference_status
    import capo_connect.types.reference_status_reason
    import capo_connect.types.reference_type
    import capo_connect.types.reference_value


class Reference(TypedDict, closed=True):
    value: "capo_connect.types.reference_value.ReferenceValue"
    """<p>A valid value for the reference. For example, for a URL reference, a formatted URL that is displayed to an agent in the Contact Control Panel (CCP).</p>"""
    type: "capo_connect.types.reference_type.ReferenceType"
    """<p>The type of the reference. <code>DATE</code> must be of type Epoch timestamp. </p>"""
    status: NotRequired["capo_connect.types.reference_status.ReferenceStatus"]
    """<p>Status of the attachment reference type.</p>"""
    arn: NotRequired["capo_connect.types.reference_arn.ReferenceArn"]
    """<p>The Amazon Resource Name (ARN) of the reference</p>"""
    status_reason: NotRequired[
        "capo_connect.types.reference_status_reason.ReferenceStatusReason"
    ]
    """<p>Relevant details why the reference was not successfully created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Reference) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", "")
    import capo_connect.types.reference_type

    out["Type"] = capo_connect.types.reference_type.serialize_json(value["type"])
    if "status" in value:
        import capo_connect.types.reference_status

        out["Status"] = capo_connect.types.reference_status.serialize_json(
            value["status"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> Reference:
    out: Reference = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("Type") is not None:
        import capo_connect.types.reference_type

        out["type"] = capo_connect.types.reference_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_connect.types.reference_type.ReferenceType", "")
    if data.get("Status") is not None:
        import capo_connect.types.reference_status

        out["status"] = capo_connect.types.reference_status.deserialize_json(
            data["Status"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    return out
