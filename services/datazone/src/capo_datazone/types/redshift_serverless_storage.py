"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftServerlessStorage``."""

from typing_extensions import TypedDict


class RedshiftServerlessStorage(TypedDict, closed=True):
    workgroup_name: "str"
    """<p>The name of the Amazon Redshift Serverless workgroup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftServerlessStorage) -> dict:
    out: dict = {}
    out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_json(data: dict) -> RedshiftServerlessStorage:
    out: RedshiftServerlessStorage = {}  # type: ignore[typeddict-item]
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        out["workgroup_name"] = ""
    return out
