"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ThrottleConfig``."""

from typing_extensions import NotRequired, TypedDict


class ThrottleConfig(TypedDict, closed=True):
    rate_limit: NotRequired["int"]
    """<p>The maximum request rate per second for the endpoint. The value must be one of the following supported values: <code>0</code>, <code>100</code>, <code>200</code>, <code>300</code>, <code>400</code>, <code>500</code>, <code>600</code>, <code>700</code>, <code>800</code>, <code>900</code>, <code>1000</code>, <code>2000</code>, <code>3000</code>, <code>4000</code>, <code>5000</code>, <code>6000</code>, <code>7000</code>, <code>8000</code>, <code>9000</code>, or <code>10000</code>. The maximum effective value is also bounded by your account-level maximum total rate limit. There is no default value. If you don't specify a value, the throttling configuration is absent from the response. On an update, omit <code>throttleConfig</code> to keep the current value, or specify an empty object to clear a previously set value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottleConfig) -> dict:
    out: dict = {}
    if "rate_limit" in value:
        out["rateLimit"] = value["rate_limit"]
    return out


def deserialize_json(data: dict) -> ThrottleConfig:
    out: ThrottleConfig = {}  # type: ignore[typeddict-item]
    if data.get("rateLimit") is not None:
        out["rate_limit"] = data["rateLimit"]
    return out
