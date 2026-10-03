"""Generated from Smithy shape ``com.amazonaws.wafv2#JsonMatchPattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.all
    import capo_wafv2.types.json_pointer_paths


class JsonMatchPattern(TypedDict, closed=True):
    all: NotRequired["capo_wafv2.types.all.All"]
    """<p>Match all of the elements. See also <code>MatchScope</code> in <a>JsonBody</a>. </p> <p>You must specify either this setting or the <code>IncludedPaths</code> setting, but not both.</p>"""
    included_paths: NotRequired["capo_wafv2.types.json_pointer_paths.JsonPointerPaths"]
    """<p>Match only the specified include paths. See also <code>MatchScope</code> in <a>JsonBody</a>. </p> <p>Provide the include paths using JSON Pointer syntax. For example, <code>"IncludedPaths": ["/dogs/0/name", "/dogs/1/name"]</code>. For information about this syntax, see the Internet Engineering Task Force (IETF) documentation <a href="https://tools.ietf.org/html/rfc6901">JavaScript Object Notation (JSON) Pointer</a>. </p> <p>You must specify either this setting or the <code>All</code> setting, but not both.</p> <note> <p>Don't use this option to include all paths. Instead, use the <code>All</code> setting. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JsonMatchPattern) -> dict:
    out: dict = {}
    if "all" in value:
        import capo_wafv2.types.all

        out["All"] = capo_wafv2.types.all.serialize_aws_json_1_1(value["all"])
    if "included_paths" in value:
        import capo_wafv2.types.json_pointer_paths

        out["IncludedPaths"] = (
            capo_wafv2.types.json_pointer_paths.serialize_aws_json_1_1(
                value["included_paths"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JsonMatchPattern:
    out: JsonMatchPattern = {}  # type: ignore[typeddict-item]
    if data.get("All") is not None:
        import capo_wafv2.types.all

        out["all"] = capo_wafv2.types.all.deserialize_aws_json_1_1(data["All"])
    if data.get("IncludedPaths") is not None:
        import capo_wafv2.types.json_pointer_paths

        out["included_paths"] = (
            capo_wafv2.types.json_pointer_paths.deserialize_aws_json_1_1(
                data["IncludedPaths"]
            )
        )
    return out
