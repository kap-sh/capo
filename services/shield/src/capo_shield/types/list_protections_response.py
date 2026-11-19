"""Generated from Smithy shape ``com.amazonaws.shield#ListProtectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protections
    import capo_shield.types.token


class ListProtectionsResponse(TypedDict, closed=True):
    protections: NotRequired["capo_shield.types.protections.Protections"]
    """<p>The array of enabled <a>Protection</a> objects.</p>"""
    next_token: NotRequired["capo_shield.types.token.Token"]
    """<p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProtectionsResponse) -> dict:
    out: dict = {}
    if "protections" in value:
        import capo_shield.types.protections

        out["Protections"] = capo_shield.types.protections.serialize_aws_json_1_1(
            value["protections"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProtectionsResponse:
    out: ListProtectionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Protections") is not None:
        import capo_shield.types.protections

        out["protections"] = capo_shield.types.protections.deserialize_aws_json_1_1(
            data["Protections"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProtectionsResponse) -> dict:
    out: dict = {}
    if "protections" in value:
        import capo_shield.types.protections

        out["Protections"] = capo_shield.types.protections.serialize_cbor(
            value["protections"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListProtectionsResponse:
    out: ListProtectionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Protections") is not None:
        import capo_shield.types.protections

        out["protections"] = capo_shield.types.protections.deserialize_cbor(
            data["Protections"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
