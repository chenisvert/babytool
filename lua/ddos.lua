--还在测试的脚本

-- 封禁IP地址的函数
max_requests = 10
ip_ban_times = {}
ip_counters = {}

local function ban_ip(ip)
    -- 这里可以添加封禁IP地址的逻辑，比如使用系统命令或调用防火墙软件
    -- 这里只是简单地输出封禁信息
    print("IP地址 " .. ip .. " 被封禁了 " .. ban_time .. " 秒")
    os.execute("iptables -A INPUT -s " .. ip .. " -j DROP")
end
local function unban_ip(ip)
    os.execute("iptables -A INPUT -s " .. ip .. " -j ACCEPT")
end
-- 检查封禁IP地址是否需要封
local function check_unban_ip(ip)
    -- 在这添加解封条件的辑，例如封禁时间是否已过期
    -- 这里设封禁时间为 60 秒
    if ip_ban_times[ip] and os() - ip_ban_times[ip] >= 60 then
        -- 解封 IP址
        unban_ip(ip)
        -- 清除封禁时间记录
        ip_ban_times[ip] = nil
    end
end

-- 获取客户端IP地址的函数
local function get_client_ip()
    return os.getenv("REMOTE_ADDR")
end

-- 获取IP的请求数，如果不存在返回0
local function get_ip_requests(ip)
    return ip_counters[ip] or 0
end

-- 增加IP地址的请求计数
local function increment_ip_requests(ip)
    ip_counters[ip] = (ip_counters[ip] or 0) + 1
end

-- 主逻辑
local function main()
    local client_ip = get_client_ip()

    -- 增加客户端IP地址的请求计数
    increment_ip_requests(client_ip)

    -- 检查是否达到最大请求限制
    if get_ip_requests(client_ip) > max_requests then
        -- 如果超过最大请求限制，封禁IP地址
        ban_ip(client_ip)
        ip_ban_times[client_ip] = os.time()
        print("DDoS攻击检测：IP地址 " .. client_ip .. " 的请求超过限制，已封禁。")
    else
        print("请求通过：IP地址 " .. client_ip .. "。")
    end
end

-- 执行主逻辑
main()
