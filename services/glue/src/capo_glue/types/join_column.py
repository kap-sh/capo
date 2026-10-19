"""Generated from Smithy shape ``com.amazonaws.glue#JoinColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_studio_path_list

JoinColumn = TypedDict(
    "JoinColumn",
    {
        "from": "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty",
        "keys": "capo_glue.types.glue_studio_path_list.GlueStudioPathList",
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JoinColumn) -> dict:
    out: dict = {}
    out["From"] = value["from"]
    import capo_glue.types.glue_studio_path_list

    out["Keys"] = capo_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
        value["keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> JoinColumn:
    out: JoinColumn = {}  # type: ignore[typeddict-item]
    if data.get("From") is not None:
        out["from"] = data["From"]
    else:
        out["from"] = ""
    if data.get("Keys") is not None:
        import capo_glue.types.glue_studio_path_list

        out["keys"] = capo_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
            data["Keys"]
        )
    else:
        out["keys"] = []
    return out
