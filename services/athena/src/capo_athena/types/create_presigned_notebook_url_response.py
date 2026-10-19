"""Generated from Smithy shape ``com.amazonaws.athena#CreatePresignedNotebookUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.auth_token
    import capo_athena.types.long
    import capo_athena.types.string


class CreatePresignedNotebookUrlResponse(TypedDict, closed=True):
    notebook_url: "capo_athena.types.string.String"
    """<p>The URL of the notebook. The URL includes the authentication token and notebook file name and points directly to the opened notebook.</p>"""
    auth_token: "capo_athena.types.auth_token.AuthToken"
    """<p>The authentication token for the notebook.</p>"""
    auth_token_expiration_time: "capo_athena.types.long.Long"
    """<p>The UTC epoch time when the authentication token expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedNotebookUrlResponse) -> dict:
    out: dict = {}
    out["NotebookUrl"] = value["notebook_url"]
    out["AuthToken"] = value["auth_token"]
    out["AuthTokenExpirationTime"] = value["auth_token_expiration_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedNotebookUrlResponse:
    out: CreatePresignedNotebookUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("NotebookUrl") is not None:
        out["notebook_url"] = data["NotebookUrl"]
    else:
        out["notebook_url"] = ""
    if data.get("AuthToken") is not None:
        out["auth_token"] = data["AuthToken"]
    else:
        out["auth_token"] = ""
    if data.get("AuthTokenExpirationTime") is not None:
        out["auth_token_expiration_time"] = data["AuthTokenExpirationTime"]
    else:
        out["auth_token_expiration_time"] = 0
    return out
