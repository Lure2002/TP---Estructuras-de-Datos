#Iniciando el TP
from datetime import date
from clases.Hospital import Hospital
hospital = Hospital()  # Crea una instancia de la clase Hospital
while True:
    print("\n--- Menú ---")
    print("1. Agregar paciente")
    print("2. Remover paciente")
    print("3. Buscar paciente")
    print("4. Agregar paciente a la guardia")
    print("5. Eliminar paciente de la guardia (atendido)")
    print("6. Eliminar paciente de la guardia (se fue)")
    print("7. Modificar datos de paciente")
    print("8. Agregar datos de paciente")
    print("9. Eliminar enfermedad de paciente")
    print("10. Eliminar medicamento de paciente")
    print("11. Agregar consulta a paciente")
    print("12. Mostrar pacientes en guardia")
    print("13. Imprimir árbol binario de pacientes")
    print("14. Mostrar historial de paciente")
    print("15. Salir")

    opcion = input("Ingrese una opción: ")  # Solicita una opción al usuario
    opcion = int(opcion)  # Convierte la opción a un entero
    if opcion == 1:  # Agregar paciente
          id_paciente = int(input("Ingrese el ID del paciente: "))
          nombre = input("Ingrese el nombre del paciente: ")
          añonac = input("Ingrese la año de nac: ")
          mesnac = input("Ingrese el mes de nac(siendo: 1,2,...,10,11,12): ")
          dia = input("Ingrese el dia de nac(siendo: 1,2,...,30): ")
          fechanac = date(int(añonac),int(mesnac),int(dia))
          sexo = input("Ingrese el sexo del paciente(masculino, femenino, x): ")
          enfermedades = []
          medicamentos = []
          while True:
            print("ingrese las enfermedades del paciente existentes, ingrese 0 para terminar")
            enfermedad = input("ingrese enfermedad:")
            if enfermedad == "0":
              break
            else:
              enfermedades.append(enfermedad)
          while True:
            print("ingrese los medicamentos del paciente existentes, ingrese 0 para terminar")
            enfermedad = input("ingrese enfermedad:")
            if enfermedad == "0":
              break
            else:
              medicamentos.append(enfermedad)
          hospital.agregarpaciente(id_paciente, nombre, fechanac, sexo, enfermedades,medicamentos)
    elif opcion == 2:  # Remover paciente
            id_paciente = int(input("Ingrese el ID del paciente a remover: "))
            hospital.removerpaciente(id_paciente)
    elif opcion == 3:  # Buscar paciente
        id_paciente = int(input("Ingrese el ID del paciente a buscar: "))
        hospital.mostrarpaciente(id_paciente)
    elif opcion == 4:  # Agregar paciente a la guardia
        id_paciente = int(input("Ingrese el ID del paciente: "))
        nombre = input("Ingrese el nombre del paciente: ")
        añonac = input("Ingrese la año de nac: ")
        mesnac = input("Ingrese el mes de nac(siendo: 1,2,...,10,11,12): ")
        dia = input("Ingrese el dia de nac(siendo: 1,2,...,30): ")
        fechanac = date(int(añonac),int(mesnac),int(dia))
        sexo = input("Ingrese el sexo del paciente(masculino, femenino, x): ")
        enfermedades = []
        medicamentos = []
        while True:
          print("ingrese las enfermedades del paciente existentes, ingrese 0 para terminar")
          enfermedad = input("ingrese enfermedad:")
          if enfermedad == "0":
            break
          else:
            enfermedades.append(enfermedad)
        while True:
          print("ingrese los medicamentos del paciente existentes, ingrese 0 para terminar")
          medicamentos = input("ingrese medicamentos:")
          if medicamentos == "0":
            break
          else:
            medicamentos.append(medicamentos)
        condicion = None
        while True:
          condicion = input("ingrese la condicion del paciente(grave, moderado, no_urgente):")
          if condicion == "grave" or condicion == "moderado" or condicion == "no_urgente":
            break
          else:
            print("ingrese una condicion valida")
        hospital.agregarpacienteguardia(id_paciente, nombre, fechanac, sexo, enfermedades,medicamentos,condicion)
    elif opcion == 5:  # Eliminar paciente de la guardia (atendido)
          hospital.eliminarpacienteguardiaatendido()
    elif opcion == 6:  # Eliminar paciente de la guardia (se fue)
          id_paciente = int(input("Ingrese el ID del paciente: "))
          hospital.eliminarpacienteguardia(id_paciente)
    elif opcion == 7:  # Modificar datos de paciente
          id_paciente = int(input("Ingrese el ID del paciente a modificar: "))
          elegiropcion = int(input("ingrese 0 si se quiere modificar el nombre y ingrese 1 si quiere modificar el sexo "))
          if elegiropcion == 0:
            while True:
              sexo = input("Ingrese el sexo del paciente(masculino, femenino): ")
              if sexo == "masculino" or sexo == "femenino" or sexo == "x":
                hospital.modificardatos(id_paciente,"sexo",sexo)
                break
              else:
                print("ingrese un sexo valido")
          elif elegiropcion == 1: 
              nombre = input("Ingrese el nombre")
              hospital.modificardatos(id_paciente,"nombre",nombre)
          else:
            print("ingrese una opcion valida")
    elif opcion == 8:  # Agregar datos de paciente medicamentos o enfermedades
          id_paciente = int(input("Ingrese el ID del paciente: "))
          elegiropcion = int(input("ingrese 0 si se quiere agregar enfermedad y ingrese 1 si quiere agregar medicamento"))
          if elegiropcion == 0:
              enfermedad = input("Ingrese la enfermedad: ")
              hospital.agregardatos(id_paciente,"enfermedad",enfermedad)
          elif elegiropcion == 1: 
              medicamento = input("Ingrese el medicamento: ")
              hospital.agregardatos(id_paciente,"medicamento",medicamento)
          else:
            print("ingrese una opcion valida")
    elif opcion == 9:  # Eliminar enfermedad de paciente
          id_paciente = int(input("Ingrese el ID del paciente: "))
          enfermedad = input("Ingrese la enfermedad a eliminar: ")
          hospital.eliminar_enfermedad(id_paciente,enfermedad)
    elif opcion == 10:  # Eliminar medicamento de paciente
          id_paciente = int(input("Ingrese el ID del paciente: "))
          medicamento = input("Ingrese el medicamento a eliminar: ")
          hospital.eliminar_medicamento(id_paciente,medicamento)
    elif opcion == 11:  # Agregar consulta a paciente
          id_paciente = int(input("Ingrese el ID del paciente: "))
          consulta = input("Ingrese la descripción de la consulta: ")
          diagnostico = input("Ingrese el diagnóstico: ")
          tratamiento = input("Ingrese el tratamiento: ")
          medicamento = []
          while True:
            print("ingrese los medicamentos del paciente recetados, ingrese 0 para terminar")
            medicamentos = input("ingrese medicamentos:")
            if medicamentos == "0":
              break
            else:
              medicamentos.append(medicamentos)
          hospital.agregar_consulta(id_paciente,consulta,diagnostico,tratamiento,medicamento)
    elif opcion == 12:  # Mostrar pacientes guardias
          hospital.mostrarguardia()
    elif opcion == 13:  # Imprimir árbol binario de pacientes
          hospital.imprimirarbolbi()
    elif opcion == 14:  # Mostrar historial de paciente
        id_paciente = int(input("Ingrese el ID del paciente: "))
        hospital. mostrar_historial_paciente(id_paciente)
    elif opcion == 15:  # Salir
          break  # Sale del bucle principal
    else:  # Opción inválida
        print("Opción inválida. Por favor, ingrese una opción válida.")