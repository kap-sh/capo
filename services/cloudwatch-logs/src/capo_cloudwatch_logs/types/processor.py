"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Processor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.add_keys
    import capo_cloudwatch_logs.types.copy_value
    import capo_cloudwatch_logs.types.csv
    import capo_cloudwatch_logs.types.date_time_converter
    import capo_cloudwatch_logs.types.delete_keys
    import capo_cloudwatch_logs.types.grok
    import capo_cloudwatch_logs.types.list_to_map
    import capo_cloudwatch_logs.types.lower_case_string
    import capo_cloudwatch_logs.types.move_keys
    import capo_cloudwatch_logs.types.parse_cloudfront
    import capo_cloudwatch_logs.types.parse_json
    import capo_cloudwatch_logs.types.parse_key_value
    import capo_cloudwatch_logs.types.parse_postgres
    import capo_cloudwatch_logs.types.parse_route53
    import capo_cloudwatch_logs.types.parse_to_ocsf
    import capo_cloudwatch_logs.types.parse_vpc
    import capo_cloudwatch_logs.types.parse_waf
    import capo_cloudwatch_logs.types.rename_keys
    import capo_cloudwatch_logs.types.split_string
    import capo_cloudwatch_logs.types.substitute_string
    import capo_cloudwatch_logs.types.trim_string
    import capo_cloudwatch_logs.types.type_converter
    import capo_cloudwatch_logs.types.upper_case_string


class Processor(TypedDict, closed=True):
    add_keys: NotRequired["capo_cloudwatch_logs.types.add_keys.AddKeys"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKeys"> addKeys</a> processor in your transformer.</p>"""
    copy_value: NotRequired["capo_cloudwatch_logs.types.copy_value.CopyValue"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-copyValue"> copyValue</a> processor in your transformer.</p>"""
    csv: NotRequired["capo_cloudwatch_logs.types.csv.CSV"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-CSV"> CSV</a> processor in your transformer.</p>"""
    date_time_converter: NotRequired[
        "capo_cloudwatch_logs.types.date_time_converter.DateTimeConverter"
    ]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-datetimeConverter"> datetimeConverter</a> processor in your transformer.</p>"""
    delete_keys: NotRequired["capo_cloudwatch_logs.types.delete_keys.DeleteKeys"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-deleteKeys"> deleteKeys</a> processor in your transformer.</p>"""
    grok: NotRequired["capo_cloudwatch_logs.types.grok.Grok"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-grok"> grok</a> processor in your transformer.</p>"""
    list_to_map: NotRequired["capo_cloudwatch_logs.types.list_to_map.ListToMap"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap"> listToMap</a> processor in your transformer.</p>"""
    lower_case_string: NotRequired[
        "capo_cloudwatch_logs.types.lower_case_string.LowerCaseString"
    ]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-lowerCaseString"> lowerCaseString</a> processor in your transformer.</p>"""
    move_keys: NotRequired["capo_cloudwatch_logs.types.move_keys.MoveKeys"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKeys"> moveKeys</a> processor in your transformer.</p>"""
    parse_cloudfront: NotRequired[
        "capo_cloudwatch_logs.types.parse_cloudfront.ParseCloudfront"
    ]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseCloudfront"> parseCloudfront</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    parse_json: NotRequired["capo_cloudwatch_logs.types.parse_json.ParseJSON"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseJSON"> parseJSON</a> processor in your transformer.</p>"""
    parse_key_value: NotRequired[
        "capo_cloudwatch_logs.types.parse_key_value.ParseKeyValue"
    ]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseKeyValue"> parseKeyValue</a> processor in your transformer.</p>"""
    parse_route53: NotRequired["capo_cloudwatch_logs.types.parse_route53.ParseRoute53"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseRoute53"> parseRoute53</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    parse_to_ocsf: NotRequired["capo_cloudwatch_logs.types.parse_to_ocsf.ParseToOCSF"]
    """<p>Use this parameter to convert logs into Open Cybersecurity Schema (OCSF) format.</p>"""
    parse_postgres: NotRequired[
        "capo_cloudwatch_logs.types.parse_postgres.ParsePostgres"
    ]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parsePostGres"> parsePostGres</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    parse_vpc: NotRequired["capo_cloudwatch_logs.types.parse_vpc.ParseVPC"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseVPC"> parseVPC</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    parse_waf: NotRequired["capo_cloudwatch_logs.types.parse_waf.ParseWAF"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseWAF"> parseWAF</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    rename_keys: NotRequired["capo_cloudwatch_logs.types.rename_keys.RenameKeys"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKeys"> renameKeys</a> processor in your transformer.</p>"""
    split_string: NotRequired["capo_cloudwatch_logs.types.split_string.SplitString"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-splitString"> splitString</a> processor in your transformer.</p>"""
    substitute_string: NotRequired[
        "capo_cloudwatch_logs.types.substitute_string.SubstituteString"
    ]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-substituteString"> substituteString</a> processor in your transformer.</p>"""
    trim_string: NotRequired["capo_cloudwatch_logs.types.trim_string.TrimString"]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-trimString"> trimString</a> processor in your transformer.</p>"""
    type_converter: NotRequired[
        "capo_cloudwatch_logs.types.type_converter.TypeConverter"
    ]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-typeConverter"> typeConverter</a> processor in your transformer.</p>"""
    upper_case_string: NotRequired[
        "capo_cloudwatch_logs.types.upper_case_string.UpperCaseString"
    ]
    """<p>Use this parameter to include the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-upperCaseString"> upperCaseString</a> processor in your transformer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Processor) -> dict:
    out: dict = {}
    if "add_keys" in value:
        import capo_cloudwatch_logs.types.add_keys

        out["addKeys"] = capo_cloudwatch_logs.types.add_keys.serialize_aws_json_1_1(
            value["add_keys"]
        )
    if "copy_value" in value:
        import capo_cloudwatch_logs.types.copy_value

        out["copyValue"] = capo_cloudwatch_logs.types.copy_value.serialize_aws_json_1_1(
            value["copy_value"]
        )
    if "csv" in value:
        import capo_cloudwatch_logs.types.csv

        out["csv"] = capo_cloudwatch_logs.types.csv.serialize_aws_json_1_1(value["csv"])
    if "date_time_converter" in value:
        import capo_cloudwatch_logs.types.date_time_converter

        out["dateTimeConverter"] = (
            capo_cloudwatch_logs.types.date_time_converter.serialize_aws_json_1_1(
                value["date_time_converter"]
            )
        )
    if "delete_keys" in value:
        import capo_cloudwatch_logs.types.delete_keys

        out["deleteKeys"] = (
            capo_cloudwatch_logs.types.delete_keys.serialize_aws_json_1_1(
                value["delete_keys"]
            )
        )
    if "grok" in value:
        import capo_cloudwatch_logs.types.grok

        out["grok"] = capo_cloudwatch_logs.types.grok.serialize_aws_json_1_1(
            value["grok"]
        )
    if "list_to_map" in value:
        import capo_cloudwatch_logs.types.list_to_map

        out["listToMap"] = (
            capo_cloudwatch_logs.types.list_to_map.serialize_aws_json_1_1(
                value["list_to_map"]
            )
        )
    if "lower_case_string" in value:
        import capo_cloudwatch_logs.types.lower_case_string

        out["lowerCaseString"] = (
            capo_cloudwatch_logs.types.lower_case_string.serialize_aws_json_1_1(
                value["lower_case_string"]
            )
        )
    if "move_keys" in value:
        import capo_cloudwatch_logs.types.move_keys

        out["moveKeys"] = capo_cloudwatch_logs.types.move_keys.serialize_aws_json_1_1(
            value["move_keys"]
        )
    if "parse_cloudfront" in value:
        import capo_cloudwatch_logs.types.parse_cloudfront

        out["parseCloudfront"] = (
            capo_cloudwatch_logs.types.parse_cloudfront.serialize_aws_json_1_1(
                value["parse_cloudfront"]
            )
        )
    if "parse_json" in value:
        import capo_cloudwatch_logs.types.parse_json

        out["parseJSON"] = capo_cloudwatch_logs.types.parse_json.serialize_aws_json_1_1(
            value["parse_json"]
        )
    if "parse_key_value" in value:
        import capo_cloudwatch_logs.types.parse_key_value

        out["parseKeyValue"] = (
            capo_cloudwatch_logs.types.parse_key_value.serialize_aws_json_1_1(
                value["parse_key_value"]
            )
        )
    if "parse_route53" in value:
        import capo_cloudwatch_logs.types.parse_route53

        out["parseRoute53"] = (
            capo_cloudwatch_logs.types.parse_route53.serialize_aws_json_1_1(
                value["parse_route53"]
            )
        )
    if "parse_to_ocsf" in value:
        import capo_cloudwatch_logs.types.parse_to_ocsf

        out["parseToOCSF"] = (
            capo_cloudwatch_logs.types.parse_to_ocsf.serialize_aws_json_1_1(
                value["parse_to_ocsf"]
            )
        )
    if "parse_postgres" in value:
        import capo_cloudwatch_logs.types.parse_postgres

        out["parsePostgres"] = (
            capo_cloudwatch_logs.types.parse_postgres.serialize_aws_json_1_1(
                value["parse_postgres"]
            )
        )
    if "parse_vpc" in value:
        import capo_cloudwatch_logs.types.parse_vpc

        out["parseVPC"] = capo_cloudwatch_logs.types.parse_vpc.serialize_aws_json_1_1(
            value["parse_vpc"]
        )
    if "parse_waf" in value:
        import capo_cloudwatch_logs.types.parse_waf

        out["parseWAF"] = capo_cloudwatch_logs.types.parse_waf.serialize_aws_json_1_1(
            value["parse_waf"]
        )
    if "rename_keys" in value:
        import capo_cloudwatch_logs.types.rename_keys

        out["renameKeys"] = (
            capo_cloudwatch_logs.types.rename_keys.serialize_aws_json_1_1(
                value["rename_keys"]
            )
        )
    if "split_string" in value:
        import capo_cloudwatch_logs.types.split_string

        out["splitString"] = (
            capo_cloudwatch_logs.types.split_string.serialize_aws_json_1_1(
                value["split_string"]
            )
        )
    if "substitute_string" in value:
        import capo_cloudwatch_logs.types.substitute_string

        out["substituteString"] = (
            capo_cloudwatch_logs.types.substitute_string.serialize_aws_json_1_1(
                value["substitute_string"]
            )
        )
    if "trim_string" in value:
        import capo_cloudwatch_logs.types.trim_string

        out["trimString"] = (
            capo_cloudwatch_logs.types.trim_string.serialize_aws_json_1_1(
                value["trim_string"]
            )
        )
    if "type_converter" in value:
        import capo_cloudwatch_logs.types.type_converter

        out["typeConverter"] = (
            capo_cloudwatch_logs.types.type_converter.serialize_aws_json_1_1(
                value["type_converter"]
            )
        )
    if "upper_case_string" in value:
        import capo_cloudwatch_logs.types.upper_case_string

        out["upperCaseString"] = (
            capo_cloudwatch_logs.types.upper_case_string.serialize_aws_json_1_1(
                value["upper_case_string"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Processor:
    out: Processor = {}  # type: ignore[typeddict-item]
    if data.get("addKeys") is not None:
        import capo_cloudwatch_logs.types.add_keys

        out["add_keys"] = capo_cloudwatch_logs.types.add_keys.deserialize_aws_json_1_1(
            data["addKeys"]
        )
    if data.get("copyValue") is not None:
        import capo_cloudwatch_logs.types.copy_value

        out["copy_value"] = (
            capo_cloudwatch_logs.types.copy_value.deserialize_aws_json_1_1(
                data["copyValue"]
            )
        )
    if data.get("csv") is not None:
        import capo_cloudwatch_logs.types.csv

        out["csv"] = capo_cloudwatch_logs.types.csv.deserialize_aws_json_1_1(
            data["csv"]
        )
    if data.get("dateTimeConverter") is not None:
        import capo_cloudwatch_logs.types.date_time_converter

        out["date_time_converter"] = (
            capo_cloudwatch_logs.types.date_time_converter.deserialize_aws_json_1_1(
                data["dateTimeConverter"]
            )
        )
    if data.get("deleteKeys") is not None:
        import capo_cloudwatch_logs.types.delete_keys

        out["delete_keys"] = (
            capo_cloudwatch_logs.types.delete_keys.deserialize_aws_json_1_1(
                data["deleteKeys"]
            )
        )
    if data.get("grok") is not None:
        import capo_cloudwatch_logs.types.grok

        out["grok"] = capo_cloudwatch_logs.types.grok.deserialize_aws_json_1_1(
            data["grok"]
        )
    if data.get("listToMap") is not None:
        import capo_cloudwatch_logs.types.list_to_map

        out["list_to_map"] = (
            capo_cloudwatch_logs.types.list_to_map.deserialize_aws_json_1_1(
                data["listToMap"]
            )
        )
    if data.get("lowerCaseString") is not None:
        import capo_cloudwatch_logs.types.lower_case_string

        out["lower_case_string"] = (
            capo_cloudwatch_logs.types.lower_case_string.deserialize_aws_json_1_1(
                data["lowerCaseString"]
            )
        )
    if data.get("moveKeys") is not None:
        import capo_cloudwatch_logs.types.move_keys

        out["move_keys"] = (
            capo_cloudwatch_logs.types.move_keys.deserialize_aws_json_1_1(
                data["moveKeys"]
            )
        )
    if data.get("parseCloudfront") is not None:
        import capo_cloudwatch_logs.types.parse_cloudfront

        out["parse_cloudfront"] = (
            capo_cloudwatch_logs.types.parse_cloudfront.deserialize_aws_json_1_1(
                data["parseCloudfront"]
            )
        )
    if data.get("parseJSON") is not None:
        import capo_cloudwatch_logs.types.parse_json

        out["parse_json"] = (
            capo_cloudwatch_logs.types.parse_json.deserialize_aws_json_1_1(
                data["parseJSON"]
            )
        )
    if data.get("parseKeyValue") is not None:
        import capo_cloudwatch_logs.types.parse_key_value

        out["parse_key_value"] = (
            capo_cloudwatch_logs.types.parse_key_value.deserialize_aws_json_1_1(
                data["parseKeyValue"]
            )
        )
    if data.get("parseRoute53") is not None:
        import capo_cloudwatch_logs.types.parse_route53

        out["parse_route53"] = (
            capo_cloudwatch_logs.types.parse_route53.deserialize_aws_json_1_1(
                data["parseRoute53"]
            )
        )
    if data.get("parseToOCSF") is not None:
        import capo_cloudwatch_logs.types.parse_to_ocsf

        out["parse_to_ocsf"] = (
            capo_cloudwatch_logs.types.parse_to_ocsf.deserialize_aws_json_1_1(
                data["parseToOCSF"]
            )
        )
    if data.get("parsePostgres") is not None:
        import capo_cloudwatch_logs.types.parse_postgres

        out["parse_postgres"] = (
            capo_cloudwatch_logs.types.parse_postgres.deserialize_aws_json_1_1(
                data["parsePostgres"]
            )
        )
    if data.get("parseVPC") is not None:
        import capo_cloudwatch_logs.types.parse_vpc

        out["parse_vpc"] = (
            capo_cloudwatch_logs.types.parse_vpc.deserialize_aws_json_1_1(
                data["parseVPC"]
            )
        )
    if data.get("parseWAF") is not None:
        import capo_cloudwatch_logs.types.parse_waf

        out["parse_waf"] = (
            capo_cloudwatch_logs.types.parse_waf.deserialize_aws_json_1_1(
                data["parseWAF"]
            )
        )
    if data.get("renameKeys") is not None:
        import capo_cloudwatch_logs.types.rename_keys

        out["rename_keys"] = (
            capo_cloudwatch_logs.types.rename_keys.deserialize_aws_json_1_1(
                data["renameKeys"]
            )
        )
    if data.get("splitString") is not None:
        import capo_cloudwatch_logs.types.split_string

        out["split_string"] = (
            capo_cloudwatch_logs.types.split_string.deserialize_aws_json_1_1(
                data["splitString"]
            )
        )
    if data.get("substituteString") is not None:
        import capo_cloudwatch_logs.types.substitute_string

        out["substitute_string"] = (
            capo_cloudwatch_logs.types.substitute_string.deserialize_aws_json_1_1(
                data["substituteString"]
            )
        )
    if data.get("trimString") is not None:
        import capo_cloudwatch_logs.types.trim_string

        out["trim_string"] = (
            capo_cloudwatch_logs.types.trim_string.deserialize_aws_json_1_1(
                data["trimString"]
            )
        )
    if data.get("typeConverter") is not None:
        import capo_cloudwatch_logs.types.type_converter

        out["type_converter"] = (
            capo_cloudwatch_logs.types.type_converter.deserialize_aws_json_1_1(
                data["typeConverter"]
            )
        )
    if data.get("upperCaseString") is not None:
        import capo_cloudwatch_logs.types.upper_case_string

        out["upper_case_string"] = (
            capo_cloudwatch_logs.types.upper_case_string.deserialize_aws_json_1_1(
                data["upperCaseString"]
            )
        )
    return out
