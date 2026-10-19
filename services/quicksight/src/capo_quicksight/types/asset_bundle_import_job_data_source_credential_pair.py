"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceCredentialPair``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.db_username
    import capo_quicksight.types.password


class AssetBundleImportJobDataSourceCredentialPair(TypedDict, closed=True):
    username: "capo_quicksight.types.db_username.DbUsername"
    """<p>The username for the data source connection.</p>"""
    password: "capo_quicksight.types.password.Password"
    """<p>The password for the data source connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceCredentialPair) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSourceCredentialPair:
    out: AssetBundleImportJobDataSourceCredentialPair = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        out["password"] = ""
    return out
