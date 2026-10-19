"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RenewalTermConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.boolean


class RenewalTermConfiguration(TypedDict, closed=True):
    enable_auto_renew: "capo_marketplace_agreement.types.boolean.Boolean"
    """<p>Defines whether the acceptor has chosen to auto-renew the agreement when it reaches its end date. Can be set to <code>True</code> or <code>False</code>. The acceptor can change this value within the limits set by <code>LockoutPeriod</code> and <code>MaxRenewals</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RenewalTermConfiguration) -> dict:
    out: dict = {}
    out["enableAutoRenew"] = value["enable_auto_renew"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RenewalTermConfiguration:
    out: RenewalTermConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enableAutoRenew") is not None:
        out["enable_auto_renew"] = data["enableAutoRenew"]
    else:
        out["enable_auto_renew"] = False
    return out
