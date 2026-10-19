"""Generated from Smithy shape ``com.amazonaws.connecthealth#DomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.domain_arn
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.domain_name
    import capo_connecthealth.types.domain_status


class DomainSummary(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the Domain.</p>"""
    arn: "capo_connecthealth.types.domain_arn.DomainArn"
    """<p/>"""
    name: "capo_connecthealth.types.domain_name.DomainName"
    """<p/>"""
    status: "capo_connecthealth.types.domain_status.DomainStatus"
    """<p/>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the Domain was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_connecthealth.types.domain_status

    out["status"] = capo_connecthealth.types.domain_status.serialize_json(
        value["status"]
    )
    import capo_connecthealth.types._prelude.timestamp

    out["createdAt"] = capo_connecthealth.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_connecthealth.types.domain_status

        out["status"] = capo_connecthealth.types.domain_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connecthealth.types.domain_status.DomainStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["created_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
