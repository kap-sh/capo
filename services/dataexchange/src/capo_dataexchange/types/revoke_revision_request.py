"""Generated from Smithy shape ``com.amazonaws.dataexchange#RevokeRevisionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string_min10_max512
    import capo_dataexchange.types.id


class RevokeRevisionRequest(TypedDict, closed=True):
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a revision.</p>"""
    revocation_comment: (
        "capo_dataexchange.types.__string_min10_max512.__stringMin10Max512"
    )
    """<p>A required comment to inform subscribers of the reason their access to the revision was revoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeRevisionRequest) -> dict:
    out: dict = {}
    out["RevocationComment"] = value["revocation_comment"]
    return out


def deserialize_json(data: dict) -> RevokeRevisionRequest:
    out: RevokeRevisionRequest = {}  # type: ignore[typeddict-item]
    if data.get("RevocationComment") is not None:
        out["revocation_comment"] = data["RevocationComment"]
    else:
        out["revocation_comment"] = ""
    return out
