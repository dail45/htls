from __future__ import annotations

from ..enums import *

"""
{
  "certCompressionAlgo": "",
  "connectionFlow": 0,
  "h2Settings": null,
  "h2SettingsOrder": null,
  "headerPriority": null,
  "ja3String": "",
  "keyShareCurves": null,
  "priorityFrames": null,
  "alpnProtocols": null,
  "alpsProtocols": null,
  "ECHCandidatePayloads": null,
  "ECHCandidateCipherSuites": null,
  "pseudoHeaderOrder": null,
  "supportedDelegatedCredentialsAlgorithms": null,
  "supportedSignatureAlgorithms": null,
  "supportedVersions": null
}
"""
class CustomTLSClient:
    def __init__(
        self,
        cert_compression_algo: CertCompressionAlgorithm | str = "",
        connection_flow: int = 0,
        h2_settings: dict[H2Setting | str, int] | None = None,
        h2_settings_order: list[H2Setting | str] | None = None,
        header_priority: PriorityParam | dict | None = None,
        ja3_string: str = "",
        key_share_curves: list[KeyShareCurves | str] | None = None,
        priority_frames: list[PriorityFrame | dict] | None = None,
        alpn_protocols: list[ALPNExtension | str] | None = None,
        alps_protocols: list[ALPSExtension | str] | None = None,
        ech_candidate_payloads: list[int] | None = None,
        ech_candidate_cipher_suites: list[str] | None = None,
        pseudo_header_order: list[str] | None = None,
        supported_delegated_credentials_algorithms: list[str] | None = None,
        supported_signature_algorithms: list[str] | None = None,
        supported_versions: list[str] | None = None,
    ):
        self.cert_compression_algo = cert_compression_algo
        self.connection_flow = connection_flow
        self.h2_settings = h2_settings
        self.h2_settings_order = h2_settings_order
        self.header_priority = header_priority
        self.ja3_string = ja3_string
        self.key_share_curves = key_share_curves
        self.priority_frames = priority_frames
        self.alpn_protocols = alpn_protocols
        self.alps_protocols = alps_protocols
        self.ech_candidate_payloads = ech_candidate_payloads
        self.ech_candidate_cipher_suites = ech_candidate_cipher_suites
        self.pseudo_header_order = pseudo_header_order
        self.supported_delegated_credentials_algorithms = supported_delegated_credentials_algorithms
        self.supported_signature_algorithms = supported_signature_algorithms
        self.supported_versions = supported_versions

    def to_payload(self):
        data = self.__dict__
        hp = data["header_priority"]
        pf = data["priority_frames"]
        if hp is not None and isinstance(hp, PriorityParam):
            data["header_priority"] = hp.to_payload()
        if pf is not None and isinstance(pf, PriorityFrame):
            data["priority_frames"] = pf.to_payload()
        return data



"""
{
    "streamDep": 0,
    "exclusive": false,
    "weight": 0
}
"""
class PriorityParam:
    def __init__(
            self,
            stream_dep: int = 0,
            exclusive: bool = False,
            weight: int = 0
    ):
        self.stream_dep = stream_dep
        self.exclusive = exclusive
        self.weight = weight

    def to_payload(self):
        return self.__dict__


"""
{
    "streamID": 0,
    "priorityParam": null
}
"""
class PriorityFrame:
    def __init__(
            self,
            stream_id: int = 0,
            priority_param: "PriorityParam" | dict | None = None,
    ):
        self.stream_id = stream_id
        self.priority_param = priority_param

    def to_payload(self):
        data = self.__dict__
        pp = data["priority_param"]
        if pp is not None and isinstance(pp, PriorityParam):
            data["priority_param"] = pp.to_payload()
        return data
