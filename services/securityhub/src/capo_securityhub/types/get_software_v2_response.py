"""Generated from Smithy shape ``com.amazonaws.securityhub#GetSoftwareV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.next_token
    import capo_securityhub.types.software_list


class GetSoftwareV2Response(TypedDict, closed=True):
    software: NotRequired["capo_securityhub.types.software_list.SoftwareList"]
    """<p>An array of software packages returned by the operation.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSoftwareV2Response) -> dict:
    out: dict = {}
    if "software" in value:
        import capo_securityhub.types.software_list

        out["Software"] = capo_securityhub.types.software_list.serialize_json(
            value["software"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSoftwareV2Response:
    out: GetSoftwareV2Response = {}  # type: ignore[typeddict-item]
    if data.get("Software") is not None:
        import capo_securityhub.types.software_list

        out["software"] = capo_securityhub.types.software_list.deserialize_json(
            data["Software"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
