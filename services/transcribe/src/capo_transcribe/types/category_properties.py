"""Generated from Smithy shape ``com.amazonaws.transcribe#CategoryProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.category_name
    import capo_transcribe.types.date_time
    import capo_transcribe.types.input_type
    import capo_transcribe.types.rule_list
    import capo_transcribe.types.tag_list


class CategoryProperties(TypedDict, closed=True):
    category_name: NotRequired["capo_transcribe.types.category_name.CategoryName"]
    """<p>The name of the Call Analytics category. Category names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    rules: NotRequired["capo_transcribe.types.rule_list.RuleList"]
    """<p>The rules used to define a Call Analytics category. Each category can have between 1 and 20 rules.</p>"""
    create_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics category was created.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    last_update_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics category was last updated.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-05T12:45:32.691000-07:00</code> represents 12:45 PM UTC-7 on May 5, 2022.</p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>The tags, each in the form of a key:value pair, assigned to the specified call analytics category.</p>"""
    input_type: NotRequired["capo_transcribe.types.input_type.InputType"]
    """<p>The input type associated with the specified category. <code>POST_CALL</code> refers to a category that is applied to batch transcriptions; <code>REAL_TIME</code> refers to a category that is applied to streaming transcriptions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoryProperties) -> dict:
    out: dict = {}
    if "category_name" in value:
        out["CategoryName"] = value["category_name"]
    if "rules" in value:
        import capo_transcribe.types.rule_list

        out["Rules"] = capo_transcribe.types.rule_list.serialize_aws_json_1_1(
            value["rules"]
        )
    if "create_time" in value:
        import capo_transcribe.types.date_time

        out["CreateTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "last_update_time" in value:
        import capo_transcribe.types.date_time

        out["LastUpdateTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["last_update_time"]
        )
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "input_type" in value:
        import capo_transcribe.types.input_type

        out["InputType"] = capo_transcribe.types.input_type.serialize_aws_json_1_1(
            value["input_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CategoryProperties:
    out: CategoryProperties = {}  # type: ignore[typeddict-item]
    if data.get("CategoryName") is not None:
        out["category_name"] = data["CategoryName"]
    if data.get("Rules") is not None:
        import capo_transcribe.types.rule_list

        out["rules"] = capo_transcribe.types.rule_list.deserialize_aws_json_1_1(
            data["Rules"]
        )
    if data.get("CreateTime") is not None:
        import capo_transcribe.types.date_time

        out["create_time"] = capo_transcribe.types.date_time.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if data.get("LastUpdateTime") is not None:
        import capo_transcribe.types.date_time

        out["last_update_time"] = (
            capo_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("InputType") is not None:
        import capo_transcribe.types.input_type

        out["input_type"] = capo_transcribe.types.input_type.deserialize_aws_json_1_1(
            data["InputType"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CategoryProperties) -> dict:
    out: dict = {}
    if "category_name" in value:
        out["CategoryName"] = value["category_name"]
    if "rules" in value:
        import capo_transcribe.types.rule_list

        out["Rules"] = capo_transcribe.types.rule_list.serialize_cbor(value["rules"])
    if "create_time" in value:
        import capo_transcribe.types.date_time

        out["CreateTime"] = capo_transcribe.types.date_time.serialize_cbor(
            value["create_time"]
        )
    if "last_update_time" in value:
        import capo_transcribe.types.date_time

        out["LastUpdateTime"] = capo_transcribe.types.date_time.serialize_cbor(
            value["last_update_time"]
        )
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_cbor(value["tags"])
    if "input_type" in value:
        import capo_transcribe.types.input_type

        out["InputType"] = capo_transcribe.types.input_type.serialize_cbor(
            value["input_type"]
        )
    return out


def deserialize_cbor(data: dict) -> CategoryProperties:
    out: CategoryProperties = {}  # type: ignore[typeddict-item]
    if data.get("CategoryName") is not None:
        out["category_name"] = data["CategoryName"]
    if data.get("Rules") is not None:
        import capo_transcribe.types.rule_list

        out["rules"] = capo_transcribe.types.rule_list.deserialize_cbor(data["Rules"])
    if data.get("CreateTime") is not None:
        import capo_transcribe.types.date_time

        out["create_time"] = capo_transcribe.types.date_time.deserialize_cbor(
            data["CreateTime"]
        )
    if data.get("LastUpdateTime") is not None:
        import capo_transcribe.types.date_time

        out["last_update_time"] = capo_transcribe.types.date_time.deserialize_cbor(
            data["LastUpdateTime"]
        )
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_cbor(data["Tags"])
    if data.get("InputType") is not None:
        import capo_transcribe.types.input_type

        out["input_type"] = capo_transcribe.types.input_type.deserialize_cbor(
            data["InputType"]
        )
    return out
