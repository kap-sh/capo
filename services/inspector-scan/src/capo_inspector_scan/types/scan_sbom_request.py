"""Generated from Smithy shape ``com.amazonaws.inspectorscan#ScanSbomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector_scan.types.output_format
    import capo_inspector_scan.types.sbom


class ScanSbomRequest(TypedDict, closed=True):
    sbom: "capo_inspector_scan.types.sbom.Sbom"
    """<p>The JSON file for the SBOM you want to scan. The SBOM must be in CycloneDX 1.5 format. This format limits you to passing 2000 components before throwing a <code>ValidException</code> error.</p>"""
    output_format: NotRequired["capo_inspector_scan.types.output_format.OutputFormat"]
    """<p>The output format for the vulnerability report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanSbomRequest) -> dict:
    out: dict = {}
    out["sbom"] = value["sbom"]
    if "output_format" in value:
        import capo_inspector_scan.types.output_format

        out["outputFormat"] = capo_inspector_scan.types.output_format.serialize_json(
            value["output_format"]
        )
    return out


def deserialize_json(data: dict) -> ScanSbomRequest:
    out: ScanSbomRequest = {}  # type: ignore[typeddict-item]
    if data.get("sbom") is not None:
        out["sbom"] = data["sbom"]
    else:
        out["sbom"] = None
    if data.get("outputFormat") is not None:
        import capo_inspector_scan.types.output_format

        out["output_format"] = capo_inspector_scan.types.output_format.deserialize_json(
            data["outputFormat"]
        )
    return out
