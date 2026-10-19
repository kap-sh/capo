"""Generated from Smithy shape ``com.amazonaws.securitylake#DeleteDataLakeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.region_list


class DeleteDataLakeRequest(TypedDict, closed=True):
    regions: "capo_securitylake.types.region_list.RegionList"
    """<p>The list of Regions where Security Lake is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataLakeRequest) -> dict:
    out: dict = {}
    import capo_securitylake.types.region_list

    out["regions"] = capo_securitylake.types.region_list.serialize_json(
        value["regions"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDataLakeRequest:
    out: DeleteDataLakeRequest = {}  # type: ignore[typeddict-item]
    if data.get("regions") is not None:
        import capo_securitylake.types.region_list

        out["regions"] = capo_securitylake.types.region_list.deserialize_json(
            data["regions"]
        )
    else:
        out["regions"] = []
    return out
