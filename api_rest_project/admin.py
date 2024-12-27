from django.contrib import admin

from .models import User, Project, ProjectMember, Task, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('date_joined',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at',)


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'role')
    search_fields = ('project__name', 'user__username')
    list_filter = ('role',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'priority', 'project', 'assigned_to', 'created_at', 'due_date')
    search_fields = ('title', 'project__name', 'assigned_to__username')
    list_filter = ('status', 'priority', 'created_at', 'due_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'task', 'created_at')
    search_fields = ('content', 'user__username', 'task__title')
    list_filter = ('created_at',)
