"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.finding_details
    import capo_ssm_incidents.types.finding_id


class Finding(TypedDict, closed=True):
    id: "capo_ssm_incidents.types.finding_id.FindingId"
    """<p>The ID assigned to the finding.</p>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp for when a finding was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp for when the finding was most recently updated with additional information.</p>"""
    details: NotRequired["capo_ssm_incidents.types.finding_details.FindingDetails"]
    """<p>Details about the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["creationTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_ssm_incidents.types._prelude.timestamp

    out["lastModifiedTime"] = (
        capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    if "details" in value:
        import capo_ssm_incidents.types.finding_details

        out["details"] = capo_ssm_incidents.types.finding_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("creationTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["creation_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("details") is not None:
        import capo_ssm_incidents.types.finding_details

        out["details"] = capo_ssm_incidents.types.finding_details.deserialize_json(
            data["details"]
        )
    return out
