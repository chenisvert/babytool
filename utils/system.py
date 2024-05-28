import psutil

def get_cpu_usage():
    cpu_utilization = psutil.cpu_percent(interval=1) 
    cpu_utilization =  f"{cpu_utilization:.2f}%"
    return  cpu_utilization

def get_memory_usage():
  # 获取系统内存信息
    memory_info = psutil.virtual_memory()
    # 计算内存使用率
    memory_utilization = (memory_info.used / memory_info.total) * 100
    memory_utilization =  f"{memory_utilization:.2f}%"
    return memory_utilization

def get_disk_usage():
    partitions = psutil.disk_partitions()
    disk_percentages = {}
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_percentages[partition.mountpoint] = usage.percent
        except Exception as e:
            print(f"Error reading disk {partition.mountpoint}: {e}")
    return disk_percentages

def get_system_load():
    return psutil.getloadavg()


