"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetZipContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_zip_bytes


class AssetZipContent(TypedDict, closed=True):
    zip_file: "capo_devops_agent.types.asset_zip_bytes.AssetZipBytes"
    """<p>The zip file bytes</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetZipContent) -> dict:
    out: dict = {}
    import capo_devops_agent.types.asset_zip_bytes

    out["zipFile"] = capo_devops_agent.types.asset_zip_bytes.serialize_json(
        value["zip_file"]
    )
    return out


def deserialize_json(data: dict) -> AssetZipContent:
    out: AssetZipContent = {}  # type: ignore[typeddict-item]
    if data.get("zipFile") is not None:
        import capo_devops_agent.types.asset_zip_bytes

        out["zip_file"] = capo_devops_agent.types.asset_zip_bytes.deserialize_json(
            data["zipFile"]
        )
    else:
        out["zip_file"] = b""
    return out
