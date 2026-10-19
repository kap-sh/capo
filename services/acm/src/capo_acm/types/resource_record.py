"""Generated from Smithy shape ``com.amazonaws.acm#ResourceRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.record_type
    import capo_acm.types.string


class ResourceRecord(TypedDict, closed=True):
    name: "capo_acm.types.string.String"
    """<p>The name of the DNS record to create in your domain. This is supplied by ACM.</p>"""
    type: "capo_acm.types.record_type.RecordType"
    """<p>The type of DNS record. Currently this can be <code>CNAME</code>.</p>"""
    value: "capo_acm.types.string.String"
    """<p>The value of the CNAME record to add to your DNS database. This is supplied by ACM.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceRecord) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_acm.types.record_type

    out["Type"] = capo_acm.types.record_type.serialize_aws_json_1_1(value["type"])
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceRecord:
    out: ResourceRecord = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_acm.types.record_type

        out["type"] = capo_acm.types.record_type.deserialize_aws_json_1_1(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_acm.types.record_type.RecordType", "")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
