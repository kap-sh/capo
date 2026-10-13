"""Generated from Smithy shape ``com.amazonaws.acm#DescribeAcmeAccountResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_account


class DescribeAcmeAccountResponse(TypedDict, closed=True):
    acme_account: NotRequired["capo_acm.types.acme_account.AcmeAccount"]
    """<p>The ACME account details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAcmeAccountResponse) -> dict:
    out: dict = {}
    if "acme_account" in value:
        import capo_acm.types.acme_account

        out["AcmeAccount"] = capo_acm.types.acme_account.serialize_aws_json_1_1(
            value["acme_account"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAcmeAccountResponse:
    out: DescribeAcmeAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("AcmeAccount") is not None:
        import capo_acm.types.acme_account

        out["acme_account"] = capo_acm.types.acme_account.deserialize_aws_json_1_1(
            data["AcmeAccount"]
        )
    return out


def redact_sensitive(value: DescribeAcmeAccountResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "acme_account" in value:
        import capo_acm.types.acme_account

        out["acme_account"] = capo_acm.types.acme_account.redact_sensitive(
            value["acme_account"]
        )
    return out
