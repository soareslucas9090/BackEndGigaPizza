from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from .connectionBD import *
import json

###################     CATEGORIA     ###################

@csrf_exempt
def cadastrarCategoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nome_categoria = data.get('nome_categoria')

            if nome_categoria:
                resultado = criar_categoria(nome_categoria)
                return JsonResponse({'resultado': resultado})
            else:
                return JsonResponse({'erro': 'O campo "nome_categoria" é obrigatório.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


@csrf_exempt
def editarCategoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_categoria = data.get('id_categoria')
            nome_categoria = data.get('nome_categoria')
            
            if id_categoria:
                if nome_categoria:
                    resultado = editar_categoria(id_categoria, nome_categoria)
                    return JsonResponse({'resultado': resultado})
                else:
                    return JsonResponse({'erro': 'O campo "nome_categoria" é obrigatório.'}, status=400)
            else:
                return JsonResponse({'erro': 'O campo "id_categoria" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


@csrf_exempt
def inativarCategoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_categoria = data.get('id_categoria')
            
            if id_categoria:
                inativar_categoria(id_categoria)
                return JsonResponse({'resultado': "ok"})
            else:
                return JsonResponse({'erro': 'O campo "id_categoria" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


@csrf_exempt
def ativarCategoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_categoria = data.get('id_categoria')
            
            if id_categoria:
                ativar_categoria(id_categoria)
                return JsonResponse({'resultado': "ok"})
            else:
                return JsonResponse({'erro': 'O campo "id_categoria" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


@csrf_exempt
def listarCategorias(request):
    if request.method == 'GET':
        retorno = []
        try:
            categorias = listar_categorias()
            for categoria in categorias:
                retorno.append({
                    "id_categoria":categoria[0],
                    "nome_categoria":categoria[1],
                    "is_active":categoria[2]
                    })
                
            return JsonResponse(retorno, encoder=DjangoJSONEncoder, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

@csrf_exempt
def listarCategoria(request, pk):
    if request.method == 'GET':
        retorno = []
        try:
            categorias = listar_categoria(pk)
            for categoria in categorias:
                retorno.append({
                    "id_categoria":categoria[0],
                    "nome_categoria":categoria[1],
                    "is_active":categoria[2]
                    })
                
            return JsonResponse(retorno[0], encoder=DjangoJSONEncoder, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

###################     SUBCATEGORIA     ###################

@csrf_exempt
def cadastrarSubcategoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_categoria = data.get('id_categoria')
            nome_subcategoria = data.get('nome_subcategoria')

            if nome_subcategoria:
                if id_categoria:
                    resultado = criar_subcategoria(nome_subcategoria, id_categoria)
                    return JsonResponse({'resultado': resultado})
                else:
                    return JsonResponse({'erro': 'O campo "id_categoria" é obrigatório.'}, status=400)
            else:
                return JsonResponse({'erro': 'O campo "nome_subcategoria" é obrigatório.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


@csrf_exempt
def editarSubcategoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_subcategoria = data.get('id_subcategoria')
            id_categoria = data.get('id_categoria')
            nome_subcategoria = data.get('nome_subcategoria')
            
            if id_subcategoria:
                if nome_subcategoria:
                    if id_categoria:
                        resultado = editar_subcategoria(id_subcategoria, id_categoria, nome_subcategoria)
                        return JsonResponse({'resultado': resultado})
                    else:
                        return JsonResponse({'erro': 'O campo "id_categoria" é obrigatório.'}, status=400)
                else:
                    return JsonResponse({'erro': 'O campo "nome_subcategoria" é obrigatório.'}, status=400)
            else:
                return JsonResponse({'erro': 'O campo "id_subcategoria" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


@csrf_exempt
def inativarSubcategoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_subcategoria = data.get('id_subcategoria')
            
            if id_subcategoria:
                inativar_subcategoria(id_subcategoria)
                return JsonResponse({'resultado': "ok"})
            else:
                return JsonResponse({'erro': 'O campo "id_subcategoria" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


@csrf_exempt
def ativarSubcategoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_subcategoria = data.get('id_subcategoria')
            
            if id_subcategoria:
                ativar_categoria(id_subcategoria)
                return JsonResponse({'resultado': "ok"})
            else:
                return JsonResponse({'erro': 'O campo "id_subcategoria" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


@csrf_exempt
def listarSubcategorias(request):
    if request.method == 'GET':
        retorno = []
        try:
            subcategorias = listar_subcategorias()
            for subcategoria in subcategorias:
                retorno.append({
                    "id_subcategoria":subcategoria[0],
                    "nome_subcategoria":subcategoria[1],
                    "id_categoria":subcategoria[2],
                    "is_active":subcategoria[3]
                    })
                
            return JsonResponse(retorno, encoder=DjangoJSONEncoder, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

@csrf_exempt
def listarSubcategoria(request, pk):
    if request.method == 'GET':
        retorno = []
        try:
            
            subcategorias = listar_subcategoria(pk)
            for subcategoria in subcategorias:
                retorno.append({
                "id_subcategoria":subcategoria[0],
                "nome_subcategoria":subcategoria[1],
                "id_categoria":subcategoria[2],
                "is_active":subcategoria[3]
                })
                
            return JsonResponse(retorno[0], encoder=DjangoJSONEncoder, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)