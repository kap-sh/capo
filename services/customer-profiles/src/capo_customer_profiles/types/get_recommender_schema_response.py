"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetRecommenderSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_schema_fields
    import capo_customer_profiles.types.recommender_schema_status
    import capo_customer_profiles.types.timestamp


class GetRecommenderSchemaResponse(TypedDict, closed=True):
    recommender_schema_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender schema.</p>"""
    fields: (
        "capo_customer_profiles.types.recommender_schema_fields.RecommenderSchemaFields"
    )
    """<p>A map of dataset type to column definitions included in the schema.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the recommender schema was created.</p>"""
    status: (
        "capo_customer_profiles.types.recommender_schema_status.RecommenderSchemaStatus"
    )
    """<p>The status of the recommender schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderSchemaResponse) -> dict:
    out: dict = {}
    out["RecommenderSchemaName"] = value["recommender_schema_name"]
    import capo_customer_profiles.types.recommender_schema_fields

    out["Fields"] = (
        capo_customer_profiles.types.recommender_schema_fields.serialize_json(
            value["fields"]
        )
    )
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.recommender_schema_status

    out["Status"] = (
        capo_customer_profiles.types.recommender_schema_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRecommenderSchemaResponse:
    out: GetRecommenderSchemaResponse = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderSchemaName") is not None:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    else:
        out["recommender_schema_name"] = ""
    if data.get("Fields") is not None:
        import capo_customer_profiles.types.recommender_schema_fields

        out["fields"] = (
            capo_customer_profiles.types.recommender_schema_fields.deserialize_json(
                data["Fields"]
            )
        )
    else:
        out["fields"] = {}
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Status") is not None:
        import capo_customer_profiles.types.recommender_schema_status

        out["status"] = (
            capo_customer_profiles.types.recommender_schema_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_customer_profiles.types.recommender_schema_status.RecommenderSchemaStatus",
            "",
        )
    return out
