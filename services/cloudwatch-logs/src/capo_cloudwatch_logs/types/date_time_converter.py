"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DateTimeConverter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.locale
    import capo_cloudwatch_logs.types.match_patterns
    import capo_cloudwatch_logs.types.source
    import capo_cloudwatch_logs.types.source_timezone
    import capo_cloudwatch_logs.types.target
    import capo_cloudwatch_logs.types.target_format
    import capo_cloudwatch_logs.types.target_timezone


class DateTimeConverter(TypedDict, closed=True):
    source: "capo_cloudwatch_logs.types.source.Source"
    """<p>The key to apply the date conversion to.</p>"""
    target: "capo_cloudwatch_logs.types.target.Target"
    """<p>The JSON field to store the result in.</p>"""
    target_format: NotRequired["capo_cloudwatch_logs.types.target_format.TargetFormat"]
    """<p>The datetime format to use for the converted data in the target field.</p> <p>If you omit this, the default of <code> yyyy-MM-dd'T'HH:mm:ss.SSS'Z</code> is used.</p>"""
    match_patterns: "capo_cloudwatch_logs.types.match_patterns.MatchPatterns"
    """<p>A list of patterns to match against the <code>source</code> field.</p>"""
    source_timezone: NotRequired[
        "capo_cloudwatch_logs.types.source_timezone.SourceTimezone"
    ]
    """<p>The time zone of the source field. If you omit this, the default used is the UTC zone.</p>"""
    target_timezone: NotRequired[
        "capo_cloudwatch_logs.types.target_timezone.TargetTimezone"
    ]
    """<p>The time zone of the target field. If you omit this, the default used is the UTC zone.</p>"""
    locale: NotRequired["capo_cloudwatch_logs.types.locale.Locale"]
    """<p>The locale of the source field. If you omit this, the default of <code>locale.ROOT</code> is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateTimeConverter) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["target"] = value["target"]
    if "target_format" in value:
        out["targetFormat"] = value["target_format"]
    import capo_cloudwatch_logs.types.match_patterns

    out["matchPatterns"] = (
        capo_cloudwatch_logs.types.match_patterns.serialize_aws_json_1_1(
            value["match_patterns"]
        )
    )
    if "source_timezone" in value:
        out["sourceTimezone"] = value["source_timezone"]
    if "target_timezone" in value:
        out["targetTimezone"] = value["target_timezone"]
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DateTimeConverter:
    out: DateTimeConverter = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        out["target"] = ""
    if data.get("targetFormat") is not None:
        out["target_format"] = data["targetFormat"]
    if data.get("matchPatterns") is not None:
        import capo_cloudwatch_logs.types.match_patterns

        out["match_patterns"] = (
            capo_cloudwatch_logs.types.match_patterns.deserialize_aws_json_1_1(
                data["matchPatterns"]
            )
        )
    else:
        out["match_patterns"] = []
    if data.get("sourceTimezone") is not None:
        out["source_timezone"] = data["sourceTimezone"]
    if data.get("targetTimezone") is not None:
        out["target_timezone"] = data["targetTimezone"]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    return out
