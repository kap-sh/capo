"""Generated from Smithy shape ``com.amazonaws.s3tables#CreateTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.version_token


class CreateTableResponse(TypedDict, closed=True):
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    version_token: "capo_s3tables.types.version_token.VersionToken"
    """<p>The version token of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTableResponse) -> dict:
    out: dict = {}
    out["tableARN"] = value["table_arn"]
    out["versionToken"] = value["version_token"]
    return out


def deserialize_json(data: dict) -> CreateTableResponse:
    out: CreateTableResponse = {}  # type: ignore[typeddict-item]
    if data.get("tableARN") is not None:
        out["table_arn"] = data["tableARN"]
    else:
        out["table_arn"] = ""
    if data.get("versionToken") is not None:
        out["version_token"] = data["versionToken"]
    else:
        out["version_token"] = ""
    return out
