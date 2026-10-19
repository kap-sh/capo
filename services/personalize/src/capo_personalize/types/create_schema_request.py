"""Generated from Smithy shape ``com.amazonaws.personalize#CreateSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.avro_schema
    import capo_personalize.types.domain
    import capo_personalize.types.name


class CreateSchemaRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>The name for the schema.</p>"""
    schema: "capo_personalize.types.avro_schema.AvroSchema"
    """<p>A schema in Avro JSON format.</p>"""
    domain: NotRequired["capo_personalize.types.domain.Domain"]
    """<p>The domain for the schema. If you are creating a schema for a dataset in a Domain dataset group, specify the domain you chose when you created the Domain dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSchemaRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["schema"] = value["schema"]
    if "domain" in value:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSchemaRequest:
    out: CreateSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    else:
        out["schema"] = ""
    if data.get("domain") is not None:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out
