def get_stats_from_camps(camps):
    return {
        'total': camps.count(),
        'ready': camps.filter(status=1).count(),
        'started': camps.filter(status=2).count(),
        'finished': camps.filter(status=3).count(),
    }

def get_stats_from_msgs(msgs):

    total = msgs.count()
    
    succeed = 0
    failed = 0
    
    if not total == 0:
        
        for msg in msgs:
            
            if msg.status == 200:
                succeed += 1
            else:
             failed += 1

    return {
        'total': total,
        'succeed': succeed,
        'failed': failed,
    }
    
    
