def collide(player, obj):
    if player.rect.colliderect(obj.rect):
        return True
    else: return False
