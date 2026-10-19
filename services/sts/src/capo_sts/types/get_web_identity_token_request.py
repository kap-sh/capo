"""Generated from Smithy shape ``com.amazonaws.sts#GetWebIdentityTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.jwt_algorithm_type
    import capo_sts.types.tag_list_type
    import capo_sts.types.web_identity_token_audience_list_type
    import capo_sts.types.web_identity_token_duration_seconds_type


class GetWebIdentityTokenRequest(TypedDict, closed=True):
    audience: "capo_sts.types.web_identity_token_audience_list_type.webIdentityTokenAudienceListType"
    """<p>The intended recipient of the web identity token. This value populates the <code>aud</code> claim in the JWT and should identify the service or application that will validate and use the token. The external service should verify this claim to ensure the token was intended for their use.</p>"""
    duration_seconds: NotRequired[
        "capo_sts.types.web_identity_token_duration_seconds_type.webIdentityTokenDurationSecondsType"
    ]
    """<p>The duration, in seconds, for which the JSON Web Token (JWT) will remain valid. The value can range from 60 seconds (1 minute) to 3600 seconds (1 hour). If not specified, the default duration is 300 seconds (5 minutes). The token is designed to be short-lived and should be used for proof of identity, then exchanged for credentials or short-lived tokens in the external service.</p>"""
    signing_algorithm: "capo_sts.types.jwt_algorithm_type.jwtAlgorithmType"
    """<p>The cryptographic algorithm to use for signing the JSON Web Token (JWT). Valid values are RS256 (RSA with SHA-256) and ES384 (ECDSA using P-384 curve with SHA-384). </p>"""
    tags: NotRequired["capo_sts.types.tag_list_type.tagListType"]
    """<p>An optional list of tags to include in the JSON Web Token (JWT). These tags are added as custom claims to the JWT and can be used by the downstream service for authorization decisions. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetWebIdentityTokenRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_sts.types.web_identity_token_audience_list_type

    capo_sts.types.web_identity_token_audience_list_type.serialize_query(
        value["audience"], pairs, f"{key_prefix}Audience"
    )
    if "duration_seconds" in value:
        pairs.append((f"{key_prefix}DurationSeconds", str(value["duration_seconds"])))
    pairs.append((f"{key_prefix}SigningAlgorithm", str(value["signing_algorithm"])))
    if "tags" in value:
        import capo_sts.types.tag_list_type

        capo_sts.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> GetWebIdentityTokenRequest:
    out: GetWebIdentityTokenRequest = {}  # type: ignore[typeddict-item]
    child_audience = el.find("Audience")
    if child_audience is not None:
        import capo_sts.types.web_identity_token_audience_list_type

        out["audience"] = (
            capo_sts.types.web_identity_token_audience_list_type.deserialize_query(
                child_audience
            )
        )
    else:
        out["audience"] = []
    child_duration_seconds = el.find("DurationSeconds")
    if child_duration_seconds is not None:
        out["duration_seconds"] = int(child_duration_seconds.text or "")
    child_signing_algorithm = el.find("SigningAlgorithm")
    if child_signing_algorithm is not None:
        out["signing_algorithm"] = str(child_signing_algorithm.text or "")
    else:
        out["signing_algorithm"] = ""
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_sts.types.tag_list_type

        out["tags"] = capo_sts.types.tag_list_type.deserialize_query(child_tags)
    return out
