from sqlalchemy.orm import sessionmaker
from databases.generate_task import GenerateTask

SessionLocal = sessionmaker(autocommit=False, autoflush=False)

def fetch_generate_tasks(engine):
    with SessionLocal(bind=engine) as session:
        generate_tasks = session.query(GenerateTask).all()

        # generate_tasksをcreated_atの降順に並び替える
        generate_tasks.sort(key=lambda generate_task: generate_task.created_at, reverse=True)

        # generate_tasksをGenerateTaskModelに変換する
        generate_task_models = []
        for generate_task in generate_tasks:
            generate_task_models.append(GenerateTaskModel(
                id=generate_task.id,
                user_id=generate_task.user_id,
                title=generate_task.title,
                status=generate_task.status,
                prompt=generate_task.prompt,
                negative_prompt=generate_task.negative_prompt,
                model_name=generate_task.model_name,
                created_at=generate_task.created_at,
                updated_at=generate_task.updated_at
            ))
        
        return generate_task_models

class GenerateTaskModel:
    def __init__(self, id, user_id, title, status, prompt, negative_prompt, model_name, created_at, updated_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.status = status
        self.prompt = prompt
        self.negative_prompt = negative_prompt
        self.model_name = model_name
        self.created_at = created_at
        self.updated_at = updated_at