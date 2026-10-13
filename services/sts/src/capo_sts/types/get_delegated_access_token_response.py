"""Generated from Smithy shape ``com.amazonaws.sts#GetDelegatedAccessTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.arn_type
    import capo_sts.types.credentials
    import capo_sts.types.non_negative_integer_type


class GetDelegatedAccessTokenResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_sts.types.credentials.Credentials"]
    packed_policy_size: NotRequired[
        "capo_sts.types.non_negative_integer_type.nonNegativeIntegerType"
    ]
    """<p>The percentage of the maximum policy size that is used by the session policy. The policy size is calculated as the sum of all the session policies and permission boundaries attached to the session. If the packed size exceeds 100%, the request fails.</p>"""
    assumed_principal: NotRequired["capo_sts.types.arn_type.arnType"]
    """<p>The Amazon Resource Name (ARN) of the principal that was assumed when obtaining the delegated access token. This ARN identifies the IAM entity whose permissions are granted by the temporary credentials.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDelegatedAccessTokenResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "credentials" in value:
        import capo_sts.types.credentials

        capo_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{key_prefix}Credentials"
        )
    if "packed_policy_size" in value:
        pairs.append(
            (f"{key_prefix}PackedPolicySize", str(value["packed_policy_size"]))
        )
    if "assumed_principal" in value:
        pairs.append((f"{key_prefix}AssumedPrincipal", str(value["assumed_principal"])))


def deserialize_query(el: Element) -> GetDelegatedAccessTokenResponse:
    out: GetDelegatedAccessTokenResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.deserialize_query(
            child_credentials
        )
    child_packed_policy_size = el.find("PackedPolicySize")
    if child_packed_policy_size is not None:
        out["packed_policy_size"] = int(child_packed_policy_size.text or "")
    child_assumed_principal = el.find("AssumedPrincipal")
    if child_assumed_principal is not None:
        out["assumed_principal"] = str(child_assumed_principal.text or "")
    return out


def redact_sensitive(value: GetDelegatedAccessTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.redact_sensitive(
            value["credentials"]
        )
    return out
