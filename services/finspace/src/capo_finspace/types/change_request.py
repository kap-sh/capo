"""Generated from Smithy shape ``com.amazonaws.finspace#ChangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.change_type
    import capo_finspace.types.db_path
    import capo_finspace.types.s3_path


class ChangeRequest(TypedDict, closed=True):
    change_type: "capo_finspace.types.change_type.ChangeType"
    """<p>Defines the type of change request. A <code>changeType</code> can have the following values:</p> <ul> <li> <p>PUT – Adds or updates files in a database.</p> </li> <li> <p>DELETE – Deletes files in a database.</p> </li> </ul>"""
    s3_path: NotRequired["capo_finspace.types.s3_path.S3Path"]
    """<p>Defines the S3 path of the source file that is required to add or update files in a database.</p>"""
    db_path: "capo_finspace.types.db_path.DbPath"
    """<p>Defines the path within the database directory. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeRequest) -> dict:
    out: dict = {}
    import capo_finspace.types.change_type

    out["changeType"] = capo_finspace.types.change_type.serialize_json(
        value["change_type"]
    )
    if "s3_path" in value:
        out["s3Path"] = value["s3_path"]
    out["dbPath"] = value["db_path"]
    return out


def deserialize_json(data: dict) -> ChangeRequest:
    out: ChangeRequest = {}  # type: ignore[typeddict-item]
    if data.get("changeType") is not None:
        import capo_finspace.types.change_type

        out["change_type"] = capo_finspace.types.change_type.deserialize_json(
            data["changeType"]
        )
    else:
        import typing

        out["change_type"] = typing.cast(
            "capo_finspace.types.change_type.ChangeType", ""
        )
    if data.get("s3Path") is not None:
        out["s3_path"] = data["s3Path"]
    if data.get("dbPath") is not None:
        out["db_path"] = data["dbPath"]
    else:
        out["db_path"] = ""
    return out
