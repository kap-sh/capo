"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerDomain``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.domain_name


class PartnerDomain(TypedDict, closed=True):
    domain_name: "capo_partnercentral_account.types.domain_name.DomainName"
    """<p>The domain name that has been verified for the partner account.</p>"""
    registered_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the domain was registered and verified for the partner account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerDomain) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    import capo_partnercentral_account.types.date_time

    out["RegisteredAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["registered_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PartnerDomain:
    out: PartnerDomain = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("RegisteredAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["registered_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["RegisteredAt"]
            )
        )
    else:
        import datetime

        out["registered_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
