"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Assertion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assertion_source
    import capo_resiliencehubv2.types.assertion_text
    import capo_resiliencehubv2.types.uuid


class Assertion(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    assertion_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The unique identifier of the assertion.</p>"""
    text: "capo_resiliencehubv2.types.assertion_text.AssertionText"
    """<p>The text content of the assertion.</p>"""
    source: "capo_resiliencehubv2.types.assertion_source.AssertionSource"
    """<p>The source of the assertion, indicating whether it was AI-generated or created by a user.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the assertion was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the assertion was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Assertion) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["assertionId"] = value["assertion_id"]
    out["text"] = value["text"]
    import capo_resiliencehubv2.types.assertion_source

    out["source"] = capo_resiliencehubv2.types.assertion_source.serialize_json(
        value["source"]
    )
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Assertion:
    out: Assertion = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("assertionId") is not None:
        out["assertion_id"] = data["assertionId"]
    else:
        out["assertion_id"] = ""
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("source") is not None:
        import capo_resiliencehubv2.types.assertion_source

        out["source"] = capo_resiliencehubv2.types.assertion_source.deserialize_json(
            data["source"]
        )
    else:
        import typing

        out["source"] = typing.cast(
            "capo_resiliencehubv2.types.assertion_source.AssertionSource", ""
        )
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
