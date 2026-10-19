"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TerraformSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.s3_url


class TerraformSource(TypedDict, closed=True):
    s3_state_file_url: "capo_resiliencehub.types.s3_url.S3Url"
    """<p> The URL of the Terraform s3 state file you need to import. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerraformSource) -> dict:
    out: dict = {}
    out["s3StateFileUrl"] = value["s3_state_file_url"]
    return out


def deserialize_json(data: dict) -> TerraformSource:
    out: TerraformSource = {}  # type: ignore[typeddict-item]
    if data.get("s3StateFileUrl") is not None:
        out["s3_state_file_url"] = data["s3StateFileUrl"]
    else:
        out["s3_state_file_url"] = ""
    return out
