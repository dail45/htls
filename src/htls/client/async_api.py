from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from htls.client import AuthBase

from htls.client import AsyncSession
from htls.cffi import CustomTLSClient
from htls.cffi.objects.request import TransportOptions


async def arequest(
        method: str,
        url: str,
        params: dict[str, str] = None,
        data: Any | None = None,
        headers: dict[str, str] = None,
        cookies: dict[str, str] = None,
        auth: "AuthBase" = None,
        timeout: float = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] = None,
        hooks: dict[str, Callable | Sequence[Callable]] = None,
        verify: bool = False,
        json: dict | list | None = None,

        force_http1: bool = False,
        header_order: list[str] | None = None,
        request_host_override: str | None = None,
        server_name_overwrite: str | None = None,
        stream_output_block_size: int | None = None,
        stream_output_eof_symbol: str | None = None,
        stream_output_path: str | None = None,
        return_request: bool = False,

        tls_client_identifier: str = "",
        custom_tls_client: CustomTLSClient | dict | None = None,

        catch_panics: bool = False,
        certificate_pinning_hosts: dict | None = None,
        transport_options: TransportOptions | dict | None = None,
        default_headers: dict[str, list[str]] | None = None,
        connect_headers: dict[str, list[str]] | None = None,
        disable_ipv6: bool = False,
        disable_ipv4: bool = False,
        local_address: str | None = None,
        session_id: str | None = None,
        with_debug: bool = False,
        with_default_cookie_jar: bool = False,
        without_cookie_jar: bool = False,
        with_random_tls_extension_order: bool = False,
        max_redirects: int = 30
):
    async with AsyncSession(tls_client_identifier, custom_tls_client, catch_panics, certificate_pinning_hosts,
                            transport_options,
                            default_headers, connect_headers, disable_ipv6, disable_ipv4, local_address, session_id,
                            with_debug,
                            with_default_cookie_jar, without_cookie_jar, with_random_tls_extension_order,
                            max_redirects) as session:
        return await session.request(
            method, url, params, data, headers, cookies, auth, timeout, allow_redirects, proxies, hooks, verify, json,
            force_http1, header_order, request_host_override, server_name_overwrite,
            stream_output_block_size, stream_output_eof_symbol, stream_output_path, return_request
        )


async def aget(
        url: str,
        params: dict[str, str] = None,
        headers: dict[str, str] = None,
        cookies: dict[str, str] = None,
        auth: "AuthBase" = None,
        timeout: float = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] = None,
        hooks: dict[str, Callable | Sequence[Callable]] = None,
        verify: bool = False,

        force_http1: bool = False,
        header_order: list[str] | None = None,
        request_host_override: str | None = None,
        server_name_overwrite: str | None = None,
        stream_output_block_size: int | None = None,
        stream_output_eof_symbol: str | None = None,
        stream_output_path: str | None = None,
        return_request: bool = False,

        tls_client_identifier: str = "",
        custom_tls_client: CustomTLSClient | dict | None = None,

        catch_panics: bool = False,
        certificate_pinning_hosts: dict | None = None,
        transport_options: TransportOptions | dict | None = None,
        default_headers: dict[str, list[str]] | None = None,
        connect_headers: dict[str, list[str]] | None = None,
        disable_ipv6: bool = False,
        disable_ipv4: bool = False,
        local_address: str | None = None,
        session_id: str | None = None,
        with_debug: bool = False,
        with_default_cookie_jar: bool = False,
        without_cookie_jar: bool = False,
        with_random_tls_extension_order: bool = False,
        max_redirects: int = 30
):
    return await arequest("GET", url, params, None, headers, cookies, auth, timeout, allow_redirects, proxies, hooks,
                          verify, None, force_http1, header_order, request_host_override, server_name_overwrite,
                          stream_output_block_size, stream_output_eof_symbol, stream_output_path, return_request,
                          tls_client_identifier, custom_tls_client, catch_panics, certificate_pinning_hosts,
                          transport_options,
                          default_headers, connect_headers, disable_ipv6, disable_ipv4, local_address, session_id,
                          with_debug,
                          with_default_cookie_jar, without_cookie_jar, with_random_tls_extension_order, max_redirects)


async def aoptions(
        url: str,
        params: dict[str, str] = None,
        data: Any | None = None,
        headers: dict[str, str] = None,
        cookies: dict[str, str] = None,
        auth: "AuthBase" = None,
        timeout: float = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] = None,
        hooks: dict[str, Callable | Sequence[Callable]] = None,
        verify: bool = False,
        json: dict | list | None = None,

        force_http1: bool = False,
        header_order: list[str] | None = None,
        request_host_override: str | None = None,
        server_name_overwrite: str | None = None,
        stream_output_block_size: int | None = None,
        stream_output_eof_symbol: str | None = None,
        stream_output_path: str | None = None,
        return_request: bool = False,

        tls_client_identifier: str = "",
        custom_tls_client: CustomTLSClient | dict | None = None,

        catch_panics: bool = False,
        certificate_pinning_hosts: dict | None = None,
        transport_options: TransportOptions | dict | None = None,
        default_headers: dict[str, list[str]] | None = None,
        connect_headers: dict[str, list[str]] | None = None,
        disable_ipv6: bool = False,
        disable_ipv4: bool = False,
        local_address: str | None = None,
        session_id: str | None = None,
        with_debug: bool = False,
        with_default_cookie_jar: bool = False,
        without_cookie_jar: bool = False,
        with_random_tls_extension_order: bool = False,
        max_redirects: int = 30
):
    return await arequest("OPTIONS", url, params, data, headers, cookies, auth, timeout, allow_redirects, proxies,
                          hooks, verify, json, force_http1, header_order, request_host_override, server_name_overwrite,
                          stream_output_block_size, stream_output_eof_symbol, stream_output_path, return_request,
                          tls_client_identifier, custom_tls_client, catch_panics, certificate_pinning_hosts,
                          transport_options,
                          default_headers, connect_headers, disable_ipv6, disable_ipv4, local_address, session_id,
                          with_debug,
                          with_default_cookie_jar, without_cookie_jar, with_random_tls_extension_order, max_redirects)


async def ahead(
        url: str,
        params: dict[str, str] = None,
        headers: dict[str, str] = None,
        cookies: dict[str, str] = None,
        auth: "AuthBase" = None,
        timeout: float = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] = None,
        hooks: dict[str, Callable | Sequence[Callable]] = None,
        verify: bool = False,

        force_http1: bool = False,
        header_order: list[str] | None = None,
        request_host_override: str | None = None,
        server_name_overwrite: str | None = None,
        stream_output_block_size: int | None = None,
        stream_output_eof_symbol: str | None = None,
        stream_output_path: str | None = None,
        return_request: bool = False,

        tls_client_identifier: str = "",
        custom_tls_client: CustomTLSClient | dict | None = None,

        catch_panics: bool = False,
        certificate_pinning_hosts: dict | None = None,
        transport_options: TransportOptions | dict | None = None,
        default_headers: dict[str, list[str]] | None = None,
        connect_headers: dict[str, list[str]] | None = None,
        disable_ipv6: bool = False,
        disable_ipv4: bool = False,
        local_address: str | None = None,
        session_id: str | None = None,
        with_debug: bool = False,
        with_default_cookie_jar: bool = False,
        without_cookie_jar: bool = False,
        with_random_tls_extension_order: bool = False,
        max_redirects: int = 30
):
    return await arequest("HEAD", url, params, None, headers, cookies, auth, timeout, allow_redirects, proxies,
                          hooks, verify, None, force_http1, header_order, request_host_override, server_name_overwrite,
                          stream_output_block_size, stream_output_eof_symbol, stream_output_path, return_request,
                          tls_client_identifier, custom_tls_client, catch_panics, certificate_pinning_hosts,
                          transport_options,
                          default_headers, connect_headers, disable_ipv6, disable_ipv4, local_address, session_id,
                          with_debug,
                          with_default_cookie_jar, without_cookie_jar, with_random_tls_extension_order, max_redirects)


async def apost(
        url: str,
        params: dict[str, str] = None,
        data: Any | None = None,
        headers: dict[str, str] = None,
        cookies: dict[str, str] = None,
        auth: "AuthBase" = None,
        timeout: float = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] = None,
        hooks: dict[str, Callable | Sequence[Callable]] = None,
        verify: bool = False,
        json: dict | list | None = None,

        force_http1: bool = False,
        header_order: list[str] | None = None,
        request_host_override: str | None = None,
        server_name_overwrite: str | None = None,
        stream_output_block_size: int | None = None,
        stream_output_eof_symbol: str | None = None,
        stream_output_path: str | None = None,
        return_request: bool = False,

        tls_client_identifier: str = "",
        custom_tls_client: CustomTLSClient | dict | None = None,

        catch_panics: bool = False,
        certificate_pinning_hosts: dict | None = None,
        transport_options: TransportOptions | dict | None = None,
        default_headers: dict[str, list[str]] | None = None,
        connect_headers: dict[str, list[str]] | None = None,
        disable_ipv6: bool = False,
        disable_ipv4: bool = False,
        local_address: str | None = None,
        session_id: str | None = None,
        with_debug: bool = False,
        with_default_cookie_jar: bool = False,
        without_cookie_jar: bool = False,
        with_random_tls_extension_order: bool = False,
        max_redirects: int = 30
):
    return await arequest("POST", url, params, data, headers, cookies, auth, timeout, allow_redirects, proxies, hooks,
                          verify, json, force_http1, header_order, request_host_override, server_name_overwrite,
                          stream_output_block_size, stream_output_eof_symbol, stream_output_path, return_request,
                          tls_client_identifier, custom_tls_client, catch_panics, certificate_pinning_hosts,
                          transport_options,
                          default_headers, connect_headers, disable_ipv6, disable_ipv4, local_address, session_id,
                          with_debug,
                          with_default_cookie_jar, without_cookie_jar, with_random_tls_extension_order, max_redirects)


async def aput(
        url: str,
        params: dict[str, str] = None,
        data: Any | None = None,
        headers: dict[str, str] = None,
        cookies: dict[str, str] = None,
        auth: "AuthBase" = None,
        timeout: float = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] = None,
        hooks: dict[str, Callable | Sequence[Callable]] = None,
        verify: bool = False,
        json: dict | list | None = None,

        force_http1: bool = False,
        header_order: list[str] | None = None,
        request_host_override: str | None = None,
        server_name_overwrite: str | None = None,
        stream_output_block_size: int | None = None,
        stream_output_eof_symbol: str | None = None,
        stream_output_path: str | None = None,
        return_request: bool = False,

        tls_client_identifier: str = "",
        custom_tls_client: CustomTLSClient | dict | None = None,

        catch_panics: bool = False,
        certificate_pinning_hosts: dict | None = None,
        transport_options: TransportOptions | dict | None = None,
        default_headers: dict[str, list[str]] | None = None,
        connect_headers: dict[str, list[str]] | None = None,
        disable_ipv6: bool = False,
        disable_ipv4: bool = False,
        local_address: str | None = None,
        session_id: str | None = None,
        with_debug: bool = False,
        with_default_cookie_jar: bool = False,
        without_cookie_jar: bool = False,
        with_random_tls_extension_order: bool = False,
        max_redirects: int = 30
):
    return await arequest("PUT", url, params, data, headers, cookies, auth, timeout, allow_redirects, proxies, hooks,
                          verify, json, force_http1, header_order, request_host_override, server_name_overwrite,
                          stream_output_block_size, stream_output_eof_symbol, stream_output_path, return_request,
                          tls_client_identifier, custom_tls_client, catch_panics, certificate_pinning_hosts,
                          transport_options,
                          default_headers, connect_headers, disable_ipv6, disable_ipv4, local_address, session_id,
                          with_debug,
                          with_default_cookie_jar, without_cookie_jar, with_random_tls_extension_order, max_redirects)


async def apatch(
        url: str,
        params: dict[str, str] = None,
        data: Any | None = None,
        headers: dict[str, str] = None,
        cookies: dict[str, str] = None,
        auth: "AuthBase" = None,
        timeout: float = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] = None,
        hooks: dict[str, Callable | Sequence[Callable]] = None,
        verify: bool = False,
        json: dict | list | None = None,

        force_http1: bool = False,
        header_order: list[str] | None = None,
        request_host_override: str | None = None,
        server_name_overwrite: str | None = None,
        stream_output_block_size: int | None = None,
        stream_output_eof_symbol: str | None = None,
        stream_output_path: str | None = None,
        return_request: bool = False,

        tls_client_identifier: str = "",
        custom_tls_client: CustomTLSClient | dict | None = None,

        catch_panics: bool = False,
        certificate_pinning_hosts: dict | None = None,
        transport_options: TransportOptions | dict | None = None,
        default_headers: dict[str, list[str]] | None = None,
        connect_headers: dict[str, list[str]] | None = None,
        disable_ipv6: bool = False,
        disable_ipv4: bool = False,
        local_address: str | None = None,
        session_id: str | None = None,
        with_debug: bool = False,
        with_default_cookie_jar: bool = False,
        without_cookie_jar: bool = False,
        with_random_tls_extension_order: bool = False,
        max_redirects: int = 30
):
    return await arequest("PATCH", url, params, data, headers, cookies, auth, timeout, allow_redirects, proxies, hooks,
                          verify, json, force_http1, header_order, request_host_override, server_name_overwrite,
                          stream_output_block_size, stream_output_eof_symbol, stream_output_path, return_request,
                          tls_client_identifier, custom_tls_client, catch_panics, certificate_pinning_hosts,
                          transport_options,
                          default_headers, connect_headers, disable_ipv6, disable_ipv4, local_address, session_id,
                          with_debug,
                          with_default_cookie_jar, without_cookie_jar, with_random_tls_extension_order, max_redirects)


async def adelete(
        url: str,
        params: dict[str, str] = None,
        data: Any | None = None,
        headers: dict[str, str] = None,
        cookies: dict[str, str] = None,
        auth: "AuthBase" = None,
        timeout: float = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] = None,
        hooks: dict[str, Callable | Sequence[Callable]] = None,
        verify: bool = False,
        json: dict | list | None = None,

        force_http1: bool = False,
        header_order: list[str] | None = None,
        request_host_override: str | None = None,
        server_name_overwrite: str | None = None,
        stream_output_block_size: int | None = None,
        stream_output_eof_symbol: str | None = None,
        stream_output_path: str | None = None,
        return_request: bool = False,

        tls_client_identifier: str = "",
        custom_tls_client: CustomTLSClient | dict | None = None,

        catch_panics: bool = False,
        certificate_pinning_hosts: dict | None = None,
        transport_options: TransportOptions | dict | None = None,
        default_headers: dict[str, list[str]] | None = None,
        connect_headers: dict[str, list[str]] | None = None,
        disable_ipv6: bool = False,
        disable_ipv4: bool = False,
        local_address: str | None = None,
        session_id: str | None = None,
        with_debug: bool = False,
        with_default_cookie_jar: bool = False,
        without_cookie_jar: bool = False,
        with_random_tls_extension_order: bool = False,
        max_redirects: int = 30
):
    return await arequest("DELETE", url, params, data, headers, cookies, auth, timeout, allow_redirects, proxies, hooks,
                          verify, json, force_http1, header_order, request_host_override, server_name_overwrite,
                          stream_output_block_size, stream_output_eof_symbol, stream_output_path, return_request,
                          tls_client_identifier, custom_tls_client, catch_panics, certificate_pinning_hosts,
                          transport_options,
                          default_headers, connect_headers, disable_ipv6, disable_ipv4, local_address, session_id,
                          with_debug,
                          with_default_cookie_jar, without_cookie_jar, with_random_tls_extension_order, max_redirects)
