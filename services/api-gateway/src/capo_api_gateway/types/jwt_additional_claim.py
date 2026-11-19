"""Generated from Smithy shape ``com.amazonaws.apigateway#JwtAdditionalClaim``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.jwt_claim_format
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.string


class JwtAdditionalClaim(TypedDict, closed=True):
    claim_name: "capo_api_gateway.types.string.String"
    """<p>The name of the claim to check. The value cannot be empty and cannot be <code>iss</code>, <code>aud</code>, <code>exp</code>, <code>nbf</code>, <code>iat</code>, <code>scope</code>, or <code>scp</code>.</p>"""
    format: "capo_api_gateway.types.jwt_claim_format.JwtClaimFormat"
    """<p>The format of the claim value. The only valid value is <code>SINGLE_STRING</code>.</p>"""
    required: "capo_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether the claim must be present in the token. Defaults to <code>false</code>. When <code>true</code>, the token must contain the claim.</p>"""
    expected_values: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>The accepted value for the claim. The value cannot be empty. When a value is specified, the claim must match it exactly, and the match is case-sensitive. When no value is specified, the claim only has to be present.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JwtAdditionalClaim) -> dict:
    out: dict = {}
    out["claimName"] = value["claim_name"]
    import capo_api_gateway.types.jwt_claim_format

    out["format"] = capo_api_gateway.types.jwt_claim_format.serialize_json(
        value["format"]
    )
    out["required"] = value.get("required", False)
    if "expected_values" in value:
        import capo_api_gateway.types.list_of_string

        out["expectedValues"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["expected_values"]
        )
    return out


def deserialize_json(data: dict) -> JwtAdditionalClaim:
    out: JwtAdditionalClaim = {}  # type: ignore[typeddict-item]
    if data.get("claimName") is not None:
        out["claim_name"] = data["claimName"]
    else:
        out["claim_name"] = ""
    if data.get("format") is not None:
        import capo_api_gateway.types.jwt_claim_format

        out["format"] = capo_api_gateway.types.jwt_claim_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_api_gateway.types.jwt_claim_format.JwtClaimFormat", ""
        )
    if data.get("required") is not None:
        out["required"] = data["required"]
    else:
        out["required"] = False
    if data.get("expectedValues") is not None:
        import capo_api_gateway.types.list_of_string

        out["expected_values"] = capo_api_gateway.types.list_of_string.deserialize_json(
            data["expectedValues"]
        )
    return out
