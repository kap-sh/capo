"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftSelfGrantStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.self_grant_status_details


class RedshiftSelfGrantStatusOutput(TypedDict, closed=True):
    self_grant_status_details: (
        "capo_datazone.types.self_grant_status_details.SelfGrantStatusDetails"
    )
    """<p>The details for the self granting status for an Amazon Redshift data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftSelfGrantStatusOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.self_grant_status_details

    out["selfGrantStatusDetails"] = (
        capo_datazone.types.self_grant_status_details.serialize_json(
            value["self_grant_status_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedshiftSelfGrantStatusOutput:
    out: RedshiftSelfGrantStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("selfGrantStatusDetails") is not None:
        import capo_datazone.types.self_grant_status_details

        out["self_grant_status_details"] = (
            capo_datazone.types.self_grant_status_details.deserialize_json(
                data["selfGrantStatusDetails"]
            )
        )
    else:
        out["self_grant_status_details"] = []
    return out
