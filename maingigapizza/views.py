import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .connectionBD import *

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
                ativar_subcategoria(id_subcategoria)
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


###################     ITEM COMPRADO    ###################

#### criar_item_comprado  ####

@csrf_exempt
def criarItemComprado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nome_item_comprado = data.get('nome_item_comprado')
            preco_item_comprado = data.get('preco_item_comprado')
            quantidade_item_comprado = data.get('quantidade_item_comprado')
            unidade_item_comprado = data.get('unidade_item_comprado')

            if nome_item_comprado:
                if preco_item_comprado:
                    if quantidade_item_comprado:
                        if unidade_item_comprado:
                            resultado = criar_item_comprado(nome_item_comprado, preco_item_comprado,
                                                            quantidade_item_comprado, unidade_item_comprado)
                            return JsonResponse({'resultado': resultado})
                        else:
                            return JsonResponse({'erro': 'O campo "unidade_item_comprado" é obrigatório.'}, status=400)
                    else:
                        return JsonResponse({'erro': 'O campo "quantidade_item_comprado" é obrigatório.'}, status=400)
                else:
                    return JsonResponse({'erro': 'O campo "preco_item_comprado" é obrigatório.'}, status=400)
            else:
                return JsonResponse({'erro': 'O campo "nome_item_comprado" é obrigatório.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

#### editar_item_comprado  ####

@csrf_exempt
def editarItemComprado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_comprado_id = data.get('id_item_comprado')
            nome = data.get('nome_item_comprado')
            preco = data.get('preco_item_comprado')
            quantidade = data.get('quantidade_item_comprado')
            unidade = data.get('unidade_item_comprado')

            if item_comprado_id:
                if nome:
                    if preco:
                        if quantidade:
                            if unidade:
                                resultado = editar_item_comprado(item_comprado_id, nome, preco, quantidade, unidade)
                                return JsonResponse({'resultado': resultado})
                            else:
                                return JsonResponse({'erro': 'O campo "unidade_item_comprado" é obrigatório.'}, status=400)
                        else:
                            return JsonResponse({'erro': 'O campo "quantidade_item_comprado" é obrigatório.'}, status=400)
                    else:
                        return JsonResponse({'erro': 'O campo "preco_item_comprado" é obrigatório.'}, status=400)
                else:
                    return JsonResponse({'erro': 'O campo "nome_item_comprado" é obrigatório.'}, status=400)
            else:
                return JsonResponse({'erro': 'O campo "id_item_comprado" é obrigatório.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

#### inativar_item_comprado  ####

@csrf_exempt
def inativarItemComprado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_item_comprado = data.get('id_item_comprado')
            
            if id_item_comprado:
                inativar_item_comprado(id_item_comprado)
                return JsonResponse({'resultado': "ok"})
            else:
                return JsonResponse({'erro': 'O campo "id_item_comprado" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

#### ativar_item_comprado ####

@csrf_exempt
def ativarItemComprado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_item_comprado = data.get('id_item_comprado')
            
            if id_item_comprado:
                ativar_item_comprado(id_item_comprado)
                return JsonResponse({'resultado': "ok"})
            else:
                return JsonResponse({'erro': 'O campo "id_item_comprado" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


#### listar_itens_comprado ####

@csrf_exempt
def listarItensComprados(request):
    if request.method == 'GET':
        retorno = []
        try:
            itens = listar_itens_comprado()
            for item in itens:
                retorno.append({
                    "id_item_comprado":item[0],
                    "nome_item_comprado":item[1],
                    "preco_item_comprado":item[2],
                    "quantidade_item_comprado":item[3],
                    "unidade_item_comprado":item[4],
                    "is_active":item[5]
                    })
                
            return JsonResponse(retorno, encoder=DjangoJSONEncoder, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

####   listar_item_comprado    ####

@csrf_exempt
def listarItemComprado(request, pk):
    if request.method == 'GET':
        retorno = []
        try:            
            itens = listar_item_comprado(pk)
            for item in itens:
                retorno.append({
                "id_item_comprado":item[0],
                "nome_item_comprado":item[1],
                "preco_item_comprado":item[2],
                "quantidade_item_comprado":item[3],
                "unidade_item_comprado":item[4],
                "is_active":item[5]
                })
                
            return JsonResponse(retorno[0], encoder=DjangoJSONEncoder, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


###################     ITEM COMPRADO    ###################

#### crari_item_venda  ####

@csrf_exempt
def criarItemVenda(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nome_item_venda = data.get('nome_item_venda')
            descricao = data.get('descricao_item_venda')
            preco = data.get('preco_item_venda')
            id_subcategoria = data.get('id_subcategoria')

            if nome_item_venda:
                if descricao:
                    if preco:
                        if id_subcategoria:
                            resultado = criar_item_venda(nome_item_venda, descricao,
                                                            preco, id_subcategoria)
                            return JsonResponse({'resultado': resultado})
                        else:
                            return JsonResponse({'erro': 'O campo "id_subcategoria" é obrigatório.'}, status=400)
                    else:
                        return JsonResponse({'erro': 'O campo "preco" é obrigatório.'}, status=400)
                else:
                    return JsonResponse({'erro': 'O campo "descricao" é obrigatório.'}, status=400)
            else:
                return JsonResponse({'erro': 'O campo "nome_item_venda" é obrigatório.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

#### editar_item_venda  ####

@csrf_exempt
def editarItemVenda(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_item_venda = data.get('id_item_venda')
            nome = data.get('nome_item_venda')
            descricao = data.get('descricao_item_venda')
            preco = data.get('preco_item_venda')

            if id_item_venda:
                if nome:
                    if descricao:
                        if preco:
                            resultado = editar_item_venda(id_item_venda, nome, descricao, preco)
                            return JsonResponse({'resultado': resultado})
                        else:
                            return JsonResponse({'erro': 'O campo "preco" é obrigatório.'}, status=400)
                    else:
                        return JsonResponse({'erro': 'O campo "descricao" é obrigatório.'}, status=400)
                else:
                    return JsonResponse({'erro': 'O campo "nome" é obrigatório.'}, status=400)
            else:
                return JsonResponse({'erro': 'O campo "id_item_venda" é obrigatório.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

#### inativar_item_venda  ####

@csrf_exempt
def inativarItemVenda(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_item_venda = data.get('id_item_venda')
            
            if id_item_venda:
                inativar_item_venda(id_item_venda)
                return JsonResponse({'resultado': "ok"})
            else:
                return JsonResponse({'erro': 'O campo "id_item_venda" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

#### ativar_item_venda ####

@csrf_exempt
def ativarItemVenda(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_item_venda = data.get('id_item_venda')
            
            if id_item_venda:
                ativar_item_comprado(id_item_venda)
                return JsonResponse({'resultado': "ok"})
            else:
                return JsonResponse({'erro': 'O campo "id_item_venda" é obrigatório.'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)


#### listar_itens_venda ####

@csrf_exempt
def listarItensVenda(request):
    if request.method == 'GET':
        retorno = []
        try:
            itens = listar_itens_venda()
            for item in itens:
                retorno.append({
                    "id_item_venda":item[0],
                    "nome_item_venda":item[1],
                    "descricao_item_venda":item[2],
                    "preco_item_venda":item[3],
                    "id_subcategoria_item_venda":item[4],
                    "is_active":item[5]
                    })
                
            return JsonResponse(retorno, encoder=DjangoJSONEncoder, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

####   listar_item_comprado    ####

@csrf_exempt
def listarItemVenda(request, pk):
    if request.method == 'GET':
        retorno = []
        try:            
            itens = listar_item_venda(pk)
            for item in itens:
                retorno.append({
                    "id_item_venda":item[0],
                    "nome_item_venda":item[1],
                    "descricao_item_venda":item[2],
                    "preco_item_venda":item[3],
                    "id_subcategoria_item_venda":item[4],
                    "is_active":item[5]
                    })
                
            return JsonResponse(retorno[0], encoder=DjangoJSONEncoder, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao decodificar o JSON.'}, status=400)

    return JsonResponse({'erro': 'Método não permitido.'}, status=405)

