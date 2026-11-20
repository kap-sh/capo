"""Generated from Smithy shape ``com.amazonaws.abusesignal#SubmissionRequirement``."""

from typing_extensions import NotRequired, TypedDict


class SubmissionRequirement(TypedDict, closed=True):
    code: NotRequired["str"]
    """<p>A stable, dot-namespaced identifier for the submission requirement that the report did not meet (for example, <code>rule.timestamp.too_old</code>). The set of codes is append-only, so treat an unrecognized value as opaque. This value is absent when the requirement that the report did not meet does not publish an identifier.</p> <p>The service checks the following submission requirements:</p> <ul> <li> <p> <code>rule.source_identifier.too_long</code> (<code>source_identifier</code>) – The value exceeds the maximum accepted length of 253 characters (the DNS hostname limit).</p> </li> <li> <p> <code>rule.source_identifier.forbidden_characters</code> (<code>source_identifier</code>) – The value contains characters that are never valid in an address (<code>{</code>, <code>}</code>, <code>*</code>, or <code>`</code>). These are common template-injection and command-injection markers.</p> </li> <li> <p> <code>rule.source_identifier.malformed</code> (<code>source_identifier</code>) – The value is not a valid IPv4 address, IPv6 address, URL, or domain name.</p> </li> <li> <p> <code>rule.timestamp.unparseable</code> (<code>timestamp</code>) – The value could not be parsed as an RFC 3339 date-time.</p> </li> <li> <p> <code>rule.timestamp.in_future</code> (<code>timestamp</code>) – The value is dated further into the future than the accepted clock-skew tolerance (a default of 1 hour).</p> </li> <li> <p> <code>rule.timestamp.too_old</code> (<code>timestamp</code>) – The value predates the submission lookback window (a default of 90 days). For content that is still accessible, set <code>timestamp</code> to the time you most recently observed it.</p> </li> <li> <p> <code>rule.evidence.content_type_mismatch</code> (<code>evidence</code>) – The decoded payload of an evidence item does not match its declared <code>content_type</code>. The <code>path</code> identifies the item, for example <code>/evidence/0</code>.</p> </li> </ul> <p>Submission requirement thresholds are configuration-driven and can change over time. The set of codes is append-only, so treat an unrecognized code as opaque.</p>"""
    path: "str"
    """<p>A JSON Pointer expression to the report member that did not meet the requirement. An empty string refers to the report as a whole.</p>"""
    message: "str"
    """<p>A detailed, human-readable description of the unmet submission requirement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmissionRequirement) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    out["path"] = value["path"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SubmissionRequirement:
    out: SubmissionRequirement = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
