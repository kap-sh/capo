"""Generated from Smithy shape ``com.amazonaws.iotwireless#CertificateList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.certificate_value
    import capo_iot_wireless.types.signing_alg


class CertificateList(TypedDict, closed=True):
    signing_alg: "capo_iot_wireless.types.signing_alg.SigningAlg"
    """<p>The certificate chain algorithm provided by sidewalk.</p>"""
    value: "capo_iot_wireless.types.certificate_value.CertificateValue"
    """<p>The value of the chosen sidewalk certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateList) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.signing_alg

    out["SigningAlg"] = capo_iot_wireless.types.signing_alg.serialize_json(
        value["signing_alg"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CertificateList:
    out: CertificateList = {}  # type: ignore[typeddict-item]
    if data.get("SigningAlg") is not None:
        import capo_iot_wireless.types.signing_alg

        out["signing_alg"] = capo_iot_wireless.types.signing_alg.deserialize_json(
            data["SigningAlg"]
        )
    else:
        import typing

        out["signing_alg"] = typing.cast(
            "capo_iot_wireless.types.signing_alg.SigningAlg", ""
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
